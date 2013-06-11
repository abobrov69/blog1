from django.conf.urls import patterns, include, url
from views import MsgListView, BlogMainView, MsgDelete, MsgUpdate, display_meta, MsgView, BlogMainViewAnchor, AboutView
from django.conf import settings
import os
from django.contrib.auth.views import login, logout
from gans_auth_views import GnsLoginFormView

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples: d
    # url(r'^$', 'blog1.views.home', name='home'),
    # url(r'^blog1/', include('blog1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url('^$', BlogMainView.as_view (), name="blogclass"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'edit/(?P<pk>\d+)/$', MsgUpdate.as_view(), name='msg_update'),
    url(r'delete/(?P<pk>\d+)/$', MsgDelete.as_view(), name='msg_delete'),
    url(r'detail/(?P<pk>\d+)/$', MsgView.as_view(), name='msg_detail'),
    url(r'post/(?P<post>\d+)/$', BlogMainViewAnchor.as_view(),name='msg_post'),
    url(r'(?P<page>\d+)/$', BlogMainView.as_view ()),
    (r'^about/$', AboutView.as_view()),
    (r'^accounts/login/$', GnsLoginFormView.as_view()),  #  login),
#    (r'^accounts/login/$', login),  #  ),
    (r'^accounts/logout/$', logout),
    )

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
         url(r'^static/(?P<path>.*)$', 'serve'),
    )
    urlpatterns += patterns('',
         (r'^meta/$', display_meta),
         url(r'^msg/$', MsgListView.as_view(), name="msglist"),
    )