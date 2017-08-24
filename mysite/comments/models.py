# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
from Posts.models import Post


class Comment(models.Model):
    user =  user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    post = models.ForeignKey(Post)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)
