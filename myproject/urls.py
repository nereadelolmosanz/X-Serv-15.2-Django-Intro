from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'myfirstapp.views.say_main',),
    url(r'^hello', 'myfirstapp.views.say_hello',),
    url(r'^bye/(.*)', 'myfirstapp.views.say_bye_to',),
    url(r'^number/(?P<number>[\d]+)', 'myfirstapp.views.say_number',),
    url(r'^admin/', include(admin.site.urls)),
)
