from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class Item(models.Model):
    created = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    last_modified = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    name = models.TextField(default='', blank=True, null=True)
    img_url = models.TextField(default='', blank=True, null=True)
    description = models.TextField(default='', blank=True, null=True)
    price = models.DecimalField(default=0, blank=True, null=True, decimal_places=2, max_digits=100)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text
