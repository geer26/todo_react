# Imports here
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Group (models.Model):
    name = models.TextField(null=False, max_length=100, blank=False)
    description = models.TextField(null=False, max_length=100, blank=True)
    users = models.ManyToManyField(CustomUser)
    created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name