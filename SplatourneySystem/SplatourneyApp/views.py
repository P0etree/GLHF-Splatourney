from django.shortcuts import render, redirect
from .models import *



def edit_schedule(request):
    return render(request,'SplatourneyApp/edit_schedule.html')

