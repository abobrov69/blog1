from django.conf.urls import patterns, include, url
from views import blog_main, AboutView, MsgListView
from django.conf import settings
from django.views.generic import TemplateView
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', blog_main, name="blogmain"),
    # Examples: d
    # url(r'^$', 'blog1.views.home', name='home'),
    # url(r'^blog1/', include('blog1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^msg/$', MsgListView.as_view()),
)
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
         url(r'^static/(?P<path>.*)$', 'serve'),
    )