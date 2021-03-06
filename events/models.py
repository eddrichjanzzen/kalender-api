import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampMixin
from django.contrib.auth.models import AbstractUser

class Event(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class EventMember(TimeStampMixin, AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    availability = models.CharField(max_length=512)
    event = models.ForeignKey(Event, related_name='event_members', on_delete=models.CASCADE)
