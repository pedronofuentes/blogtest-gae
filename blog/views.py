# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post
from blog.forms import PostForm

def get_post(request, slug):
  post = get_object_or_404(Post,slug=slug)
  return render_to_response('post_detail.html', {'post': post}, RequestContext(request))