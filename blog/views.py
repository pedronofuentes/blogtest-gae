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


def add_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      post = Post.objects.get(title=form.cleaned_data['title'])
      return HttpResponseRedirect(reverse('blog.views.get_post',args=(post.slug,)))
  
  form = PostForm()
  return render_to_response('post_form.html', {'form':form}, RequestContext(request))

def edit_post(request, slug):
  post = get_object_or_404(Post, slug=slug)
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post_edited = form.save(commit=False)
      post.title = post_edited.title
      post.body = post_edited.body
      post.author = post_edited.author
      post.save()
      return HttpResponseRedirect(reverse('blog.views.get_post',args=(post.slug,)))

  form = PostForm(instance=post)
  return render_to_response('post_form.html', {'form': form}, RequestContext(request))
  