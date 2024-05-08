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
        currentuser = Moderator.objects.filter(moderator_username=mod_name,moderator_password=mod_password)
        if not currentuser:
            return render(request, 'SplatourneyApp/login_moderator.html')
        else:
            return redirect('tournaments_screen')
    else:
        return render(request, 'SplatourneyApp/login_moderator.html')

def tournament_details(request):
    return render(request,'SplatourneyApp/tournament_details.html')
  
def player_registration(request):
    if(request.method=="POST"):
        p1_fname=request.POST.get("p1fname")
        p1_lname=request.POST.get("p1lname")
        p1_in_game_name=request.POST.get("p1ign")
        p1_dc_id=request.POST.get("p1dc")
        p1_fc=request.POST.get("p1fc")
        p1_rank=request.POST.get("p1rank")
        p1_role=request.POST.get("p1role")
        Player.objects.create(player_fname=p1_fname, player_lname=p1_lname, player_in_game_name=p1_in_game_name, player_dc_id=p1_dc_id, player_fc=p1_fc, player_rank=p1_rank, player_role=p1_role, player_type='member')
        return redirect("view_registrations")    
    else:
        return render(request, 'SplatourneyApp/player_registration.html') 

def registration_type(request):
    return render(request,'SplatourneyApp/registration_type.html')

def team_registration(request):
    if (request.method=="POST"):
        team_Name = request.POST.get('Team_Name')
        team = Team.objects.create(team_Name=team_Name, wins=0, losses=0, team_Rank=8)
        p1_fname=request.POST.get("p1fname")
        p1_lname=request.POST.get("p1lname")
        p1_in_game_name=request.POST.get("p1ign")
        p1_dc_id=request.POST.get("p1dc")
        p1_fc=request.POST.get("p1fc")
        p1_rank=request.POST.get("p1rank")
        p1_role=request.POST.get("p1role")
        p1_type=request.POST.get("p1type")
        Player.objects.create(Team_ID=team, player_fname=p1_fname, player_lname=p1_lname, player_in_game_name=p1_in_game_name, player_dc_id=p1_dc_id, player_fc=p1_fc, player_rank=p1_rank, player_role=p1_role, player_type=p1_type)
        p2_fname=request.POST.get("p2fname")
        p2_lname=request.POST.get("p2lname")
        p2_in_game_name=request.POST.get("p2ign")
        p2_dc_id=request.POST.get("p2dc")
        p2_fc=request.POST.get("p2fc")
        p2_rank=request.POST.get("p2rank")
        p2_role=request.POST.get("p2role")
        p2_type=request.POST.get("p2type")
        Player.objects.create(Team_ID=team, player_fname=p2_fname, player_lname=p2_lname, player_in_game_name=p2_in_game_name, player_dc_id=p2_dc_id, player_fc=p2_fc, player_rank=p2_rank, player_role=p2_role, player_type=p2_type)
        p3_fname=request.POST.get("p3fname")
        p3_lname=request.POST.get("p3lname")
        p3_in_game_name=request.POST.get("p3ign")
        p3_dc_id=request.POST.get("p3dc")
        p3_fc=request.POST.get("p3fc")
        p3_rank=request.POST.get("p3rank")
        p3_role=request.POST.get("p3role")
        p3_type=request.POST.get("p3type")
        Player.objects.create(Team_ID=team, player_fname=p3_fname, player_lname=p3_lname, player_in_game_name=p3_in_game_name, player_dc_id=p3_dc_id, player_fc=p3_fc, player_rank=p3_rank, player_role=p3_role, player_type=p3_type)
        p4_fname=request.POST.get("p4fname")
        p4_lname=request.POST.get("p4lname")
        p4_in_game_name=request.POST.get("p4ign")
        p4_dc_id=request.POST.get("p4dc")
        p4_fc=request.POST.get("p4fc")
        p4_rank=request.POST.get("p4rank")
        p4_role=request.POST.get("p4role")
        p4_type=request.POST.get("p4type")
        Player.objects.create(Team_ID=team, player_fname=p4_fname, player_lname=p4_lname, player_in_game_name=p4_in_game_name, player_dc_id=p4_dc_id, player_fc=p4_fc, player_rank=p4_rank, player_role=p4_role, player_type=p4_type)
        p5_fname=request.POST.get("p5fname")
        p5_lname=request.POST.get("p5lname")
        p5_in_game_name=request.POST.get("p5ign")
        p5_dc_id=request.POST.get("p5dc")
        p5_fc=request.POST.get("p5fc")
        p5_rank=request.POST.get("p5rank")
        p5_role=request.POST.get("p5role")
        p5_type=request.POST.get("p5type")
        Player.objects.create(Team_ID=team, player_fname=p5_fname, player_lname=p5_lname, player_in_game_name=p5_in_game_name, player_dc_id=p5_dc_id, player_fc=p5_fc, player_rank=p5_rank, player_role=p5_role, player_type=p5_type)
        p6_fname=request.POST.get("p6fname")
        p6_lname=request.POST.get("p6lname")
        p6_in_game_name=request.POST.get("p6ign")
        p6_dc_id=request.POST.get("p6dc")
        p6_fc=request.POST.get("p6fc")
        p6_rank=request.POST.get("p6rank")
        p6_role=request.POST.get("p6role")
        p6_type=request.POST.get("p6type")
        Player.objects.create(Team_ID=team, player_fname=p6_fname, player_lname=p6_lname, player_in_game_name=p6_in_game_name, player_dc_id=p6_dc_id, player_fc=p6_fc, player_rank=p6_rank, player_role=p6_role, player_type=p6_type)
        
        Player_objects = Player.objects.all()
        return render(request, 'SplatourneyApp/registrations.html', {'Player': Player_objects})
    
    else:
        return render(request, 'SplatourneyApp/team_registration.html')
    
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
        return redirect('tournament_details')
    else:
        return render(request, 'SplatourneyApp/create_tournament.html')

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
    gameEntry_objects = GameEntry.objects.all()
    return render(request, '#', {'gameEntry_objects': gameEntry_objects} )

def declare_winner(request, pk):
    winning_team = GameEntry.objects.get(gameEntry_Name=pk)
    winning_team_name = winning_team.getTeam_ID()
    next_pairing = winning_team.getNext_GameEntry()
    GameEntry.objects.filter(gameEntry_Name=next_pairing).update(team_ID=winning_team_name)
    Team.objects.filter(team_Name=winning_team_name).update(wins =+ 1)
    return redirect ('view_bracket')

def start_tournament(request):
    #t = pk something something
    Tournament.objects.filter(pk='t').update(registration_status='Closed', tournament_status='ongoing')
    return redirect('tournament_details')

def create_bracket_proto(request):
    Bracket.objects.all().delete()
    BracketColumn.objects.all().delete()
    Team.objects.all().delete()
    GameEntry.objects.all().delete()

    bracket = Bracket.objects.create(bracket_Name='Bracket 1')
    bracketColumn1 = BracketColumn.objects.create(bracketColumn_Name='Round 1', bracket_ID=bracket, bracketColumn_Limit=4)
    bracketColumn2 = BracketColumn.objects.create(bracketColumn_Name='Round 2', bracket_ID=bracket, bracketColumn_Limit=2)
    bracketColumn3 = BracketColumn.objects.create(bracketColumn_Name='Round 3', bracket_ID=bracket, bracketColumn_Limit=1)
    pairing1 = Pairing.objects.create(pairing_Name='1', bracketColumn_ID=bracketColumn1, pairing_Status='Not Started')
    pairing2 = Pairing.objects.create(pairing_Name='2', bracketColumn_ID=bracketColumn1, pairing_Status='Not Started')
    pairing3 = Pairing.objects.create(pairing_Name='3', bracketColumn_ID=bracketColumn1, pairing_Status='Not Started')
    pairing4 = Pairing.objects.create(pairing_Name='4', bracketColumn_ID=bracketColumn1, pairing_Status='Not Started')
    pairing5 = Pairing.objects.create(pairing_Name='5', bracketColumn_ID=bracketColumn2, pairing_Status='Not Started')
    pairing6 = Pairing.objects.create(pairing_Name='6', bracketColumn_ID=bracketColumn2, pairing_Status='Not Started')
    pairing7 = Pairing.objects.create(pairing_Name='7', bracketColumn_ID=bracketColumn3, pairing_Status='Not Started')
    team1 = Team.objects.create(team_Name='team1', wins=0, losses=0, team_Rank=8)
    team2 = Team.objects.create(team_Name='team2', wins=0, losses=0, team_Rank=8)
    team3 = Team.objects.create(team_Name='team3', wins=0, losses=0, team_Rank=8)
    team4 = Team.objects.create(team_Name='team4', wins=0, losses=0, team_Rank=8)
    team5 = Team.objects.create(team_Name='team5', wins=0, losses=0, team_Rank=8)
    team6 = Team.objects.create(team_Name='team6', wins=0, losses=0, team_Rank=8)
    team7 = Team.objects.create(team_Name='team7', wins=0, losses=0, team_Rank=8)
    team8 = Team.objects.create(team_Name='team8', wins=0, losses=0, team_Rank=8)
    gameEntry1 = GameEntry.objects.create(gameEntry_Name='gameEntry1', next_GameEntry='gameEntry9', pairing_ID=pairing1, team_ID=team1, team_Check_in_Status="NotCheckedIn")
    gameEntry2 = GameEntry.objects.create(gameEntry_Name='gameEntry2', next_GameEntry='gameEntry9', pairing_ID=pairing1, team_ID=team2, team_Check_in_Status="NotCheckedIn")
    gameEntry3 = GameEntry.objects.create(gameEntry_Name='gameEntry3', next_GameEntry='gameEntry10', pairing_ID=pairing2, team_ID=team3, team_Check_in_Status="NotCheckedIn")
    gameEntry4 = GameEntry.objects.create(gameEntry_Name='gameEntry4', next_GameEntry='gameEntry10', pairing_ID=pairing2, team_ID=team4, team_Check_in_Status="NotCheckedIn")
    gameEntry5 = GameEntry.objects.create(gameEntry_Name='gameEntry5', next_GameEntry='gameEntry11', pairing_ID=pairing3, team_ID=team5, team_Check_in_Status="NotCheckedIn")
    gameEntry6 = GameEntry.objects.create(gameEntry_Name='gameEntry6', next_GameEntry='gameEntry11', pairing_ID=pairing3, team_ID=team6, team_Check_in_Status="NotCheckedIn")
    gameEntry7 = GameEntry.objects.create(gameEntry_Name='gameEntry7', next_GameEntry='gameEntry12', pairing_ID=pairing4, team_ID=team7, team_Check_in_Status="NotCheckedIn")
    gameEntry8 = GameEntry.objects.create(gameEntry_Name='gameEntry8', next_GameEntry='gameEntry12', pairing_ID=pairing4, team_ID=team8, team_Check_in_Status="NotCheckedIn")
    gameEntry9 = GameEntry.objects.create(gameEntry_Name='gameEntry9', next_GameEntry='gameEntry13', pairing_ID=pairing5,  team_Check_in_Status="NotCheckedIn")
    gameEntry10 = GameEntry.objects.create(gameEntry_Name='gameEntry10', next_GameEntry='gameEntry13', pairing_ID=pairing5, team_Check_in_Status="NotCheckedIn")
    gameEntry11 = GameEntry.objects.create(gameEntry_Name='gameEntry11', next_GameEntry='gameEntry14', pairing_ID=pairing6, team_Check_in_Status="NotCheckedIn")
    gameEntry12 = GameEntry.objects.create(gameEntry_Name='gameEntry12', next_GameEntry='gameEntry14', pairing_ID=pairing6, team_Check_in_Status="NotCheckedIn")
    gameEntry13 = GameEntry.objects.create(gameEntry_Name='gameEntry13', pairing_ID=pairing7, team_Check_in_Status="NotCheckedIn")
    gameEntry14 = GameEntry.objects.create(gameEntry_Name='gameEntry14', pairing_ID=pairing7, team_Check_in_Status="NotCheckedIn")

    return render(request,'SplatourneyApp/create_bracket.html', {'bracketColumn1': bracketColumn1, 'bracketColumn2': bracketColumn2, 'bracketColumn3': bracketColumn3, 'pairing1': pairing1, 'pairing2': pairing2, 'pairing3': pairing3, 'pairing4': pairing4, 'pairing5': pairing5, 'pairing6': pairing6, 'pairing7': pairing7, 'gameEntry1': gameEntry1, 'gameEntry2': gameEntry2, 'gameEntry2': gameEntry2, 'gameEntry3': gameEntry3, 'gameEntry4': gameEntry4, 'gameEntry5': gameEntry5, 'gameEntry6': gameEntry6, 'gameEntry7': gameEntry7, 'gameEntry8': gameEntry8, 'gameEntry9':gameEntry9, 'gameEntry10':gameEntry10, 'gameEntry11':gameEntry11, 'gameEntry12':gameEntry12, 'gameEntry13':gameEntry13, 'gameEntry14':gameEntry14})

def create_bracket(request):                                                                                            #Function to create bracket
    Bracket.objects.create()                                                                                            
    total_team_count = 'total_team_count'                                                                               #Takes the total amount of teams
    counter = 1                                                                                                         #Divides the players by 8 (each bracket column will have 8 pairings)
    while counter < total_team_count:                                                                                   #loop to create bracket columns
        BracketColumn.objects.create(bracketColumn_Name='Column ' + counter, bracketColumn_limit=counter)
        counter = counter*2

def create_pairings(request):                                                                                           #Function to create pairings
    all_columns = BracketColumn.objects.all()                                                                           #Query to get a list of all bracket columns
    for x in all_columns:                                                                                               #Loop to make pairings in all bracket columns 
        column = BracketColumn.objects.get(pk=x)                                                                        #Get a specific bracket column using pk
        column_limit = column.bracketColumn_Limit                                                                       #Get the limit of the bracket column, to know when the loop stops making pairings
        column_id = column.pk                                                                                           #store in a variable
        for y in range(0, column_limit):                                                                                #Loop to make pairings based on the bracket column limit
            Pairing.objects.create(bracketColumn_ID=column_id, pairing_Name='Pairing ' + column_id + y, pairing_Status='Not Started')   #Creating the pairing

def create_starting_entries(request):                                                                                  #Function to create starting game entries for the teams (game entries for round 1)
    total_team_count = 'total_team_count'
    counter = 1                                                                                                        
    while counter < total_team_count:
           counter = counter*2
    start = BracketColumn.objects.get(bracketColumn_Limit=counter)                                                 
    start_ID = start.pk
    starting_pairings = Pairing.objects.all().filter(BracketColumn_ID=start_ID)
    teams = Team.objects.all()
    for x in starting_pairings:
        GameEntry.objects.create(pairing_ID=x)
        GameEntry.objects.create(pairing_ID=x)
    entries= GameEntry.objects.all()
    for y in teams:
        GameEntry.objects.filter()
    return
    
def pairing_screens(request):
    gameEntries = GameEntry.objects.all()
    return render(request, 'SplatourneyApp/pairing_screens.html', {'gameEntries':gameEntries})

def create_team(request):
    if request.method=="POST":
        Team_Name = request.POST.get('teamname')
        newteam = Team.objects.create(team_Name=Team_Name, wins=0, losses=0, team_Rank=8)
        captain = request.POST.get('captain')
        co_captain = request.POST.get('co-captain')
        member1 = request.POST.get('member1')
        member2 = request.POST.get('member2')
        member3 = request.POST.get('member3')
        member4 = request.POST.get('member4')
        Player.objects.filter(player_in_game_name=captain).update(Team_ID=newteam, player_type='captain')
        Player.objects.filter(player_in_game_name=co_captain).update(Team_ID=newteam, player_type='co-captain')
        Player.objects.filter(player_in_game_name=member1).update(Team_ID=newteam)
        Player.objects.filter(player_in_game_name=member2).update(Team_ID=newteam)
        Player.objects.filter(player_in_game_name=member3).update(Team_ID=newteam)
        Player.objects.filter(player_in_game_name=member4).update(Team_ID=newteam)
        return redirect('view_registrations')
    else:
        players = Player.objects.all().exclude(Team_ID__isnull=False)
        return render(request, "SplatourneyApp/create_team.html", {'players':players})

def tournaments_screen(request):
    return render(request, 'SplatourneyApp/tournaments_screen.html')

def edit_player_registration(request):
    return render(request,'SplatourneyApp/edit_player_registration.html')


def edit_team_registration(request):
    return render(request,'SplatourneyApp/edit_team_registration.html')


def create_moderator(request):
    return render(request,'SplatourneyApp/create_moderator.html')

def view_bracket(request):
    bracket = Bracket.objects.get(bracket_Name='Bracket 1')
    bracketColumn1 = BracketColumn.objects.get(bracketColumn_Name='Round 1')
    bracketColumn2 = BracketColumn.objects.get(bracketColumn_Name='Round 2')
    bracketColumn3 = BracketColumn.objects.get(bracketColumn_Name='Round 3')
    pairing1 = Pairing.objects.get(pairing_Name='1')
    pairing2 = Pairing.objects.get(pairing_Name='2')
    pairing3 = Pairing.objects.get(pairing_Name='3')
    pairing4 = Pairing.objects.get(pairing_Name='4')
    pairing5 = Pairing.objects.get(pairing_Name='5')
    pairing6 = Pairing.objects.get(pairing_Name='6')
    pairing7 = Pairing.objects.get(pairing_Name='7')
    team1 = Team.objects.get(team_Name='team1')
    team2 = Team.objects.get(team_Name='team2')
    team3 = Team.objects.get(team_Name='team3')
    team4 = Team.objects.get(team_Name='team4')
    team5 = Team.objects.get(team_Name='team5')
    team6 = Team.objects.get(team_Name='team6')
    team7 = Team.objects.get(team_Name='team7')
    team8 = Team.objects.get(team_Name='team8')
    gameEntry1 = GameEntry.objects.get(gameEntry_Name='gameEntry1')
    gameEntry2 = GameEntry.objects.get(gameEntry_Name='gameEntry2')
    gameEntry3 = GameEntry.objects.get(gameEntry_Name='gameEntry3')
    gameEntry4 = GameEntry.objects.get(gameEntry_Name='gameEntry4')
    gameEntry5 = GameEntry.objects.get(gameEntry_Name='gameEntry5')
    gameEntry6 = GameEntry.objects.get(gameEntry_Name='gameEntry6')
    gameEntry7 = GameEntry.objects.get(gameEntry_Name='gameEntry7')
    gameEntry8 = GameEntry.objects.get(gameEntry_Name='gameEntry8')
    gameEntry9 = GameEntry.objects.get(gameEntry_Name='gameEntry9')
    gameEntry10 = GameEntry.objects.get(gameEntry_Name='gameEntry10')
    gameEntry11 = GameEntry.objects.get(gameEntry_Name='gameEntry11')
    gameEntry12 = GameEntry.objects.get(gameEntry_Name='gameEntry12')
    gameEntry13 = GameEntry.objects.get(gameEntry_Name='gameEntry13')
    gameEntry14 = GameEntry.objects.get(gameEntry_Name='gameEntry14')

    return render(request,'SplatourneyApp/create_bracket.html', {'bracketColumn1': bracketColumn1, 'bracketColumn2': bracketColumn2, 'bracketColumn3': bracketColumn3, 'pairing1': pairing1, 'pairing2': pairing2, 'pairing3': pairing3, 'pairing4': pairing4, 'pairing5': pairing5, 'pairing6': pairing6, 'pairing7': pairing7, 'gameEntry1': gameEntry1, 'gameEntry2': gameEntry2, 'gameEntry2': gameEntry2, 'gameEntry3': gameEntry3, 'gameEntry4': gameEntry4, 'gameEntry5': gameEntry5, 'gameEntry6': gameEntry6, 'gameEntry7': gameEntry7, 'gameEntry8': gameEntry8, 'gameEntry9':gameEntry9, 'gameEntry10':gameEntry10, 'gameEntry11':gameEntry11, 'gameEntry12':gameEntry12, 'gameEntry13':gameEntry13, 'gameEntry14':gameEntry14})

def manage_moderators(request):
    return render(request,'SplatourneyApp/manage_moderators.html')
