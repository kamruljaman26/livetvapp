from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

import json

class TvLink(models.Model):
    """Database models for Live TV App"""
    tv1name = models.CharField(max_length=300, default="tvname")
    tv1link = models.CharField(max_length=300, default="tvlink")
    tv1ylink = models.CharField(max_length=300, default="youtubelink")

    tv2name = models.CharField(max_length=300, default="tvname")
    tv2link = models.CharField(max_length=300, default="tvlink")
    tv2ylink = models.CharField(max_length=300, default="youtubelink")

    tv3name = models.CharField(max_length=300, default="tvname")
    tv3link = models.CharField(max_length=300, default="tvlink")
    tv3ylink = models.CharField(max_length=300, default="youtubelink")

    tv4name = models.CharField(max_length=300, default="tvname")
    tv4link = models.CharField(max_length=300, default="tvlink")
    tv4ylink = models.CharField(max_length=300, default="youtubelink")

    tv5name = models.CharField(max_length=300, default="tvname")
    tv5link = models.CharField(max_length=300, default="tvlink")
    tv5ylink = models.CharField(max_length=300, default="youtubelink")

    def __str__(self):
        """To String Method"""
        return json.loads(self)

