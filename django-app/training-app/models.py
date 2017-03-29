from __future__ import unicode_literals

from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    phone_number2 = models.IntegerField(null=True, blank=True)
    phone_number3 = models.IntegerField(null=True, blank=True, default=0)


class History(models.Model):
    user = models.ForeignKey(User)
    login_details = models.DateTimeField()


# Signals
def add_entry_to_histry_db(sender, user, request, **kwargs):
    record = History.objects.create(user=user, login_details=datetime.now() + timedelta(hours=2))
    record.save()


# Signals handlers
user_logged_in.connect(add_entry_to_histry_db)
