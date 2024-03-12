"""
URL configuration for SplatourneySystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.player_registration, name='player_registration'),
    path('register', views.register, name='register'),
    path('team_register', views.team_register, name='team_register'),
    path('player_registration/', views.player_registration, name='player_registration'),
    path('', views.tournament_details, name='tournament_details'),
    path('tournament_details/', views.tournament_details, name='tournament_details'),
    path('team_registration/', views.team_registration, name='team_registration'),
    path('team_registration1/', views.team_registration1, name='team_registration1'),
    path('team_registration2/', views.team_registration2, name='team_registration2'),
    path('team_registration3/', views.team_registration3, name='team_registration3'),
    path('team_registration4/', views.team_registration4, name='team_registration4'),
    path('team_registration5/', views.team_registration5, name='team_registration5'),
    path('team_registration6/', views.team_registration6, name='team_registration6'),
    path('registrations/', views.view_registrations, name='view_registrations'),
    path('registration_type/', views.registration_type, name='registration_type'),

]
