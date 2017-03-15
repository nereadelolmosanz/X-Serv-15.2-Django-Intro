"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^$', 'myfirstapp.views.say_main',),
    # ^ Nada por delante
    # $ Nada por detras
    # ^$ Vacio
    #url(r'^hello', 'myfirstapp.views.say_hello',),
    url(r'^hello/(.*)', 'myfirstapp.views.say_hello',),
    # Los () indican que es un parametro.
    # Si no se incluye nombre, van por orden de apariencia.
    url(r'^bye/(.*)', 'myfirstapp.views.say_bye_to',),
    # .* Todo, cero o mas veces.
    url(r'^num/(?P<num>.*)', 'myfirstapp.views.say_num',),
    #?P<num> indica que el parametro se llama "num"
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.+', 'myfirstapp.views.resourceError',),
    # .+ Todo, una o mas veces.
]
