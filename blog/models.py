# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(510, blank=True)
  body = models.TextField()
  author = models.ForeignKey(User)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __unicode__(self):
    return u'%s' % self.title