"""kursova_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'kursova.views.start', name='main'),
    url(r'^graph/$', 'kursova.views.graph', name='graph'),
    url(r'^about/$', 'kursova.views.about', name='about'),
    url(r'^addtomap/', 'kursova.views.addtomap', name='addtomap'),
    url(r'^bubble/$', 'kursova.views.bubble', name='bubble'),
    url(r'^map/$', 'kursova.views.map', name='map'),
    url(r'^search/$', 'kursova.views.search', name='search'),
    url(r'^Search/$', 'kursova.views.Search', name='Search'),
    url(r'^contact/$', 'kursova.views.contact', name='contact'),
]
