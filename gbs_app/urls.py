"""Gas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('register', views.user_add, name='register'),
    path('staff', views.staff_login, name='staff'),
    path('user', views.user_login, name='user'),
    path('uhome', views.uhome, name='uhome'),
    path('book', views.book_refill, name='book'),
    path('u_details', views.retrive_user_details, name='u_details'),
    path('shome', views.shome, name='shome'),
    path('update', views.user_details_update, name='update'),
    path('view_booking', views.retrive_view_booking, name='view_booking'),
    path('delete', views.user_del, name="delete"),
    path('logout', views.logout, name='logout'),

]
