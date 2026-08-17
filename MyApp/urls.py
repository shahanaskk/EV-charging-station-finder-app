"""
URL configuration for EV_Charging_Stations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from MyApp import views

urlpatterns = [
    path('add_EV/',views.add_EV),
    path('admin_view_ev/',views.admin_view_ev),
    path('edit_ev_station/<id>',views.edit_ev_station),
    path('delete_ev_station/<id>',views.delete_ev_station),
    path('log_in/',views.log_in),
    path('log_inPost/',views.log_inPost),
    path('admin_home/',views.admin_home),
    path('sign_up/',views.sign_up),
    path('sign_upPost/',views.sign_upPost),
    path('user_home/',views.user_home),
    path('worker_home/',views.worker_home),
    path('manage_slots/',views.manage_slots),
    path('add_slots/',views.add_slots),
    path('ev_station_home/',views.ev_station_home),
    path('edit_slots/<id>',views.edit_slots),
    path('delete_slot/<id>',views.delete_slot)
]
