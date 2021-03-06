from django.conf.urls.defaults import *
from django.contrib import admin
from blog.urls import urlpatterns

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns += patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
)
