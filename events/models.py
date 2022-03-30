from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()