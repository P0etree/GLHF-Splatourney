from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def tournament_details(request):
    return render(request,'SplatourneyApp/tournament_details.html')
  
#Player registration - loads registration form for players
def player_registration(request):
    return render(request,'SplatourneyApp/player_registration.html')
#Registration Type - loads registration type to discern if player or team reg
def registration_type(request):
    return render(request,'SplatourneyApp/registration_type.html')

#register - takes inputs from player registration form and creates player
def register(request):
    #when submit button is pressed
    if(request.method=="POST"):
        player_fname=request.POST.get("FirstNameInput")
        player_lname=request.POST.get("LastNameInput")
        player_in_game_name=request.POST.get("ignInput")
        player_dc_id=request.POST.get("PlayerDiscordInput")
        player_fc=request.POST.get("PlayerFriendCodeInput")
        player_rank=request.POST.get("PlayerRankInput")
        
        Player.objects.create(player_fname=player_fname, player_lname=player_lname, player_in_game_name=player_in_game_name, player_dc_id=player_dc_id, player_fc=player_fc, player_rank=player_rank)

        #loads registrations screen
        Player_objects = Player.objects.all()
        return render(request, 'SplatourneyApp/registrations.html', {'Player': Player_objects})
    else:
        #loads page
        return render(request, "{% url 'player_registration' %}")

#team register - takes inputs from team registration form
#practically 6 player forms
def team_register(request):
    if(request.method=="POST"):
        p1_fname=request.POST.get("p1fname")
        p1_lname=request.POST.get("p1lname")
        p1_in_game_name=request.POST.get("p1ign")
        p1_dc_id=request.POST.get("PlayerDiscordInput")
        p1_fc=request.POST.get("PlayerFriendCodeInput")
        p1_rank=request.POST.get("p1rank")
        p1_type=request.POST.get("p1type")
        Player.objects.create(player_fname=p1_fname, player_lname=p1_lname, player_in_game_name=p1_in_game_name, player_dc_id=p1_dc_id, player_fc=p1_fc, player_rank=p1_rank, player_type=p1_type)

        p2_fname=request.POST.get("p2fname")
        p2_lname=request.POST.get("p2lname")
        p2_in_game_name=request.POST.get("p2ign")
        p2_dc_id=request.POST.get("PlayerDiscordInput")
        p2_fc=request.POST.get("PlayerFriendCodeInput")
        p2_rank=request.POST.get("p2rank")
        Player.objects.create(player_fname=p2_fname, player_lname=p2_lname, player_in_game_name=p2_in_game_name, player_dc_id=p2_dc_id, player_fc=p2_fc, player_rank=p2_rank)

        p3_fname=request.POST.get("p3fname")
        p3_lname=request.POST.get("p3lname")
        p3_in_game_name=request.POST.get("p3ign")
        p3_dc_id=request.POST.get("PlayerDiscordInput")
        p3_fc=request.POST.get("PlayerFriendCodeInput")
        p3_rank=request.POST.get("p3rank")
        Player.objects.create(player_fname=p3_fname, player_lname=p3_lname, player_in_game_name=p3_in_game_name, player_dc_id=p3_dc_id, player_fc=p3_fc, player_rank=p3_rank)

        p4_fname=request.POST.get("p4fname")
        p4_lname=request.POST.get("p4lname")
        p4_in_game_name=request.POST.get("p4ign")
        p4_dc_id=request.POST.get("PlayerDiscordInput")
        p4_fc=request.POST.get("PlayerFriendCodeInput")
        p4_rank=request.POST.get("p4rank")
        Player.objects.create(player_fname=p4_fname, player_lname=p4_lname, player_in_game_name=p4_in_game_name, player_dc_id=p4_dc_id, player_fc=p4_fc, player_rank=p4_rank)

        p5_fname=request.POST.get("p5fname")
        p5_lname=request.POST.get("p5lname")
        p5_in_game_name=request.POST.get("p5ign")
        p5_dc_id=request.POST.get("PlayerDiscordInput")
        p5_fc=request.POST.get("PlayerFriendCodeInput")
        p5_rank=request.POST.get("p5rank")
        Player.objects.create(player_fname=p5_fname, player_lname=p5_lname, player_in_game_name=p5_in_game_name, player_dc_id=p5_dc_id, player_fc=p5_fc, player_rank=p5_rank)

        p6_fname=request.POST.get("p5fname")
        p6_lname=request.POST.get("p5lname")
        p6_in_game_name=request.POST.get("p6ign")
        p6_dc_id=request.POST.get("PlayerDiscordInput")
        p6_fc=request.POST.get("PlayerFriendCodeInput")
        p6_rank=request.POST.get("p6rank")
        Player.objects.create(player_fname=p6_fname, player_lname=p6_lname, player_in_game_name=p6_in_game_name, player_dc_id=p6_dc_id, player_fc=p6_fc, player_rank=p6_rank)
        
    else:
        return render(request, "{% url 'team_registration' %}") 

def team_registration(request):
    if (request.method=="POST"):
        Team_ID = request.POST.get('Team_ID')
        Team_Name = request.POST.get('Team_Name')
    else:
        return render(request, 'SplatourneyApp/team_registration0.html')
    
def team_registration1(request):
    return render(request, 'SplatourneyApp/team_registration1.html')

def team_registration2(request):
    return render(request, 'SplatourneyApp/team_registration2.html')
    

def team_registration3(request):
   return render(request, 'SplatourneyApp/team_registration3.html')
    
def team_registration4(request):
    return render(request, 'SplatourneyApp/team_registration4.html')
    

def team_registration5(request):
     return render(request, 'SplatourneyApp/team_registration5.html')


def team_registration6(request):
     return render(request, 'SplatourneyApp/team_registration6.html')
    
def view_registrations(request):
    Player_objects = Player.objects.all()
    return render(request, 'SplatourneyApp/registrations.html', {'Player': Player_objects})

def login_page(request):
    return render(request, 'SplatourneyApp/login_page.html')