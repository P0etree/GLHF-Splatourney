from django.shortcuts import render, redirect
from .models import *



def create_bracket(request):
    return render(request,'SplatourneyApp/create_bracket.html')

