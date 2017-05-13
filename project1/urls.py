"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!");

from django.utils import timezone
def today (request):
    return HttpResponse(timezone.now());

def greeting(request, name):
    return HttpResponse("Hello, " + name);

def add(request, n1,n2):
    int(n1)
    int(n2)
    return HttpResponse(int(n1) + int(n2));

def multiply(request, num):
    int(num)
    return HttpResponse(int(num) *2);

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/',hello,name='hello'),
    url(r'^today/',today,name='today'),
    url(r'^greeting/(?P<name>[\w-]+)',greeting,name='greeting'),
    url(r'^add/(?P<n1>[\d-]+)/(?P<n2>[\d-]+)',add,name='add'),
    url(r'^multiply/(?P<num>[\d-]+)',multiply,name='multiply'),
    url(r'^forum/', include('forum.urls'), name='forum'),
    url(r'^post/', include('forum.urls'), name='post'),
    url(r'^author/', include('forum.urls'),name='author'),
]
