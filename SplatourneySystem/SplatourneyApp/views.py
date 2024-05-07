from django.shortcuts import render, redirect
from .models import *



def create_team(request):
    return render(request,'SplatourneyApp/create_team.html')

