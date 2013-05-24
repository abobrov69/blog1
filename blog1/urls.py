from django.conf.urls import patterns, include, url
from views import blog_main, hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^$', blog_main),
    # Examples:
    # url(r'^$', 'blog1.views.home', name='home'),
    # url(r'^blog1/', include('blog1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
