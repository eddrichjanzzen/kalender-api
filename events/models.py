import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampMixin

class Event(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class TimeSlot(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slot = models.DateTimeField()