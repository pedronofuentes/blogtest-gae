# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from blog.models import Post

urlpatterns = patterns('',
  ('^$', list_detail.object_list, {'queryset': Post.objects.order_by('-created'),
                                    'template_name': 'post_list.html',
                                    'template_object_name': 'post'}),
  ('^post/(?P<slug>.+)', list_detail.object_detail, {
                                    'queryset': Post.objects.all(),
                                    'slug_field': 'slug',
                                    'template_name': 'post_detail.html',
                                    'template_object_name': 'post'
  }),
)