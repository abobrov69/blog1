from django.conf.urls import patterns, include, url
from views import MsgListView, BlogMainView, MsgCreate, MsgDelete, MsgUpdate
from django.conf import settings
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', BlogMainView.as_view (), name="blogclass"),
    # Examples: d
    # url(r'^$', 'blog1.views.home', name='home'),
    # url(r'^blog1/', include('blog1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^msg/$', MsgListView.as_view(), name="msglist"),
    url(r'msg/add/$', MsgCreate.as_view(), name='msg_add'),
    url(r'msg/(?P<pk>\d+)/$', MsgUpdate.as_view(), name='msg_update'),
    url(r'msg/(?P<pk>\d+)/delete/$', MsgDelete.as_view(), name='msg_delete'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
         url(r'^static/(?P<path>.*)$', 'serve'),
    )