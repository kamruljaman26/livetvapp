from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

import json

class TvLink(models.Model):
    """Database models for Live TV App"""
    tv1name = models.CharField(max_length=300, default="Channel Name")
    tv1link = models.CharField(max_length=300, default="TV Link")
    tv1ylink = models.CharField(max_length=300, default="TV Link")

    tv2name = models.CharField(max_length=300, default="Channel Name")
    tv2link = models.CharField(max_length=300, default="TV Link")
    tv2ylink = models.CharField(max_length=300, default="TV Link")

    tv3name = models.CharField(max_length=300, default="Channel Name")
    tv3link = models.CharField(max_length=300, default="TV Link")
    tv3ylink = models.CharField(max_length=300, default="TV Link")

    tv4name = models.CharField(max_length=300, default="Channel Name")
    tv4link = models.CharField(max_length=300, default="TV Link")
    tv4ylink = models.CharField(max_length=300, default="TV Link")

    tv5name = models.CharField(max_length=300, default="Channel Name")
    tv5link = models.CharField(max_length=300, default="TV Link")
    tv5ylink = models.CharField(max_length=300, default="TV Link")

    def __str__(self):
        """To String Method"""
        return json.loads(self)

