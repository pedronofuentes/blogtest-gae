# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

def get_post(request, slug):
  post = get_object_or_404(Post,slug=slug)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
  else:
    form = CommentForm()
  return render_to_response('post_detail.html', {'post': post, 'form': form}, RequestContext(request))


def add_post(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      post = Post.objects.get(title=form.cleaned_data['title'])
      return HttpResponseRedirect(reverse('blog.views.get_post',args=(post.slug,)))
  else:
    form = PostForm()
  return render_to_response('post_form.html', {'form':form, 'new':True}, RequestContext(request))

def edit_post(request, id):
  post = get_object_or_404(Post, id=id)
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post_edited = form.save(commit=False)
      post.title = post_edited.title
      post.body = post_edited.body
      post.author = post_edited.author
      post.save()
      return HttpResponseRedirect(reverse('blog.views.get_post',args=(post.slug,)))
  else:
    form = PostForm(instance=post)
  return render_to_response('post_form.html', {'form': form, 'new':False}, RequestContext(request))

def delete_post(request, id):
  post = get_object_or_404(Post, id=id)
  for comment in post.comment_set.all():
    comment.delete()
  post.delete()
  return HttpResponseRedirect('/')

def delete_comment(request, id):
  comment = get_object_or_404(Comment, id=id)
  post = comment.post
  comment.delete()
  return HttpResponseRedirect(reverse('blog.views.get_post',args=(post.slug,)))