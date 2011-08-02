# -*- coding:utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=510, blank=True)
  body = models.TextField()
  author = models.CharField(max_length=255)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __unicode__(self):
    return u'%s' % self.title
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Post,self).save(*args, **kwargs)

class Comment(models.Model):
  post = models.ForeignKey(Post)
  author = models.CharField(max_length=255)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  
  def __unicode__(self):
    return u'Comment id:%i (Post: %s)' % (self.id, self.post.title)
  
  class Meta:
    ordering = ['created']