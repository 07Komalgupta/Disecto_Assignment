"""proapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from api.models import item
from api.serializers import itemSerializer
from api.views import apiOverview
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.apiOverview),
    path('itemlist/', views.itemList),
    path('itemdetail/<str:pk>/', views.itemDetail),
    path('itemadd/', views.itemCreate),
    path('itemupdate/<str:pk>/', views.itemUpdate),
    path('itemdelete/<str:pk>/', views.itemDelete),

    path('download/',views.download)

]
