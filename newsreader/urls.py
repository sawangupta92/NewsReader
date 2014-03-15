from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^feed_list','newsreader.nread.views.feed_list'),
	url(r'^view_feed','newsreader.nread.views.view_feed'),
	url(r'^save','newsreader.nread.views.save'),
    url(r'^annotate','newsreader.nread.views.annotate'),
    # Examples:
    # url(r'^$', 'newsreader.views.home', name='home'),
    # url(r'^newsreader/', include('newsreader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()