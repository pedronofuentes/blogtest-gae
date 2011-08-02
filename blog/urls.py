# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from blog.models import Post

urlpatterns = patterns('blog.views',
  (r'^$', list_detail.object_list, {'queryset': Post.objects.order_by('-created'),
                                    'template_name': 'post_list.html',
                                    'template_object_name': 'post'}),
  (r'^post/add$', 'add_post'),
  (r'^post/edit/(?P<slug>.+)$', 'edit_post'),
  (r'^post/(?P<slug>.+)$', 'get_post'),
)