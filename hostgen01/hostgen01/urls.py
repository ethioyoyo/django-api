
"""hostgen01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls  import url, include
from hostgenapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^api_list',views.api_list,name='api_list'),
    url(r'^api_gen/',views.api_gen,name='api_gen'),
    url(r'^hostgenapp/',include('hostgenapp.urls')),
    url(r'^special/',views.special,name='special'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^generate_api',views.generate_hosts,name='generate_hosts'),
    url('admin/', admin.site.urls),
]

