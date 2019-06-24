from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
