# -*- coding:utf-8 -*-
from django import forms
from blog.models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'body', 'author')

class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    fields = ('author','body')