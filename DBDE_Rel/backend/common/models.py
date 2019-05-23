#!/usr/bin/env python
# coding=utf-8

__author__ = 'bluven'

import time

from datetime import timedelta
from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _




class BaseModel(models.Model):

    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


