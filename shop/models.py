from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.IntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subj = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
