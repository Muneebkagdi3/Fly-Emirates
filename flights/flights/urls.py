"""
URL configuration for flights project.

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
from django.urls import path,include
from fly.views import Home
from fly.views import FlightList, FlightDetail
from .  import views
from fly import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path("list/", FlightList.as_view(), name="list" ),
    path('detail/<int:pk>', FlightDetail.as_view(), name="detail" ),
    path("register/", views.User_register, name="register" ),
    path("login/", views.User_login, name="login"),
    path("logout/", views.User_logout, name="logout"),
    path("fly/", include('fly.urls'))


]
