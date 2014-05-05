from django.conf.urls import patterns, include, url

from django.contrib import admin
import web_api

admin.autodiscover()

urlpatterns = patterns('',

    # have a home page
    url(r'^$', web_api.mainpage_view),
    
    #direct all api calls to the web_api application
    url(r'^api/', include('web_api.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
