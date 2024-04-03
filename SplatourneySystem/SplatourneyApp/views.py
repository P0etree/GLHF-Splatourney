from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def login(request):
    return render(request,'SplatourneyApp/tournament_details.html')   

def login_player(request):
    return render(request,'SplatourneyApp/tournament_details.html')

def login_moderator(request):
    if(request.method=="POST"):
        mod_name=request.POST.get("mod_name")
        mod_password=request.POST.get("mod_password")
        if Moderator.objects.filter(mod_name=mod_name, mod_password=mod_password).exists():
            return render (request,'SplatourneyApp/tournament_details.html')
        else:
            return render (request,'SplatourneyApp/tournament_details.html', {'fail':'That moderator does not exist'})
    else:
        return render(request,'SplatourneyApp/tournament_details.html')

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

def create_tournament(request):
    if request.method=="POST":
        tournament_title=request.POST.get("tournament_title")
        tournament_description=request.POST.get("tournament_description")
        tournament_mode=request.POST.get("tournament_mode")
        registration_status=request.POST.get("registration_status")
        tournament_status=request.POST.get("tournament_status")
        Tournament.objects.create(tournament_title=tournament_title, tournament_description=tournament_description, tournament_mode=tournament_mode, registration_status=registration_status, tournament_status=tournament_status)
        return redirect('tournament details screen')
    else:
        return render('tournament details screen')

def edit_tournament(request, pk):
    if request.method=="POST":
        tournament_title=request.POST.get("tournament_title")
        tournament_description=request.POST.get("tournament_description")
        tournament_mode=request.POST.get("tournament_mode")
        registration_status=request.POST.get("registration_status")
        tournament_status=request.POST.get("tournament_status")
        Tournament.objects.filter(pk=pk).update(tournament_title=tournament_title, tournament_description=tournament_description, tournament_mode=tournament_mode, registration_status=registration_status, tournament_status=tournament_status)
        return redirect()
    else:
        return render ()

def pairings(request):
    pairing_objects = Pairing.objects.all()
    return render(request, '#', {'pairing': pairing_objects} )

def declare_winner(request):
    if request.method=='POST':
        winner = 'winner'
        Team.objects.filter(team_Name=winner).update(wins=+1)
    return render ('pairings screen')

def start_tournament(request):
    #t = pk something something
    Tournament.objects.filter(pk='t').update(registration_status='Closed', tournament_status='ongoing')

def create_bracketColumns(request):
    total_player_count = 'total_player_count'
    needed_bracket_columns = total_player_count/8
    while needed_bracket_columns > 0:
        BracketColumn.objects.create(bracketColumn_Name='Round ' + needed_bracket_columns, bracketColumn_limit=8)
        needed_bracket_columns =- 1

def create_tournament(request):
     return render(request, 'SplatourneyApp/create_tournament.html')
    
def pairing_screens(request):
    return render(request, 'SplatourneyApp/pairing_screens.html')

