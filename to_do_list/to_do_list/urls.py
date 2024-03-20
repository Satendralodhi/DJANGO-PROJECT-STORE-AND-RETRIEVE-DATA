"""
URL configuration for to_do_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from to_do_list import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path("dashbord/", views.dashbord),
    path("update/<int:myid>", views.update),
    path("delete/<int:myid>", views.delete),
    path('update/u/<int:myid>',views.u)
]
