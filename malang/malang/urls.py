"""malang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from songplay.views import index
from songplay.views import search
from songplay.views import add
from songplay.views import vote,getTopRequestsJson,blankview,getNewRequestsJson


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',  index),
    url(r'^search/$',  search),
    url(r'^add/$',  add),      
    url(r'^vote/$',  vote), 
    url(r'^top/$',  getTopRequestsJson),
    url(r'^new/$',  getNewRequestsJson),
    url(r'^test2/$',  blankview),      
    url('^', include('django.contrib.auth.urls')),

    
]
