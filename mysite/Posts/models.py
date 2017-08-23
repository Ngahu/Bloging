# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Posts:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]
