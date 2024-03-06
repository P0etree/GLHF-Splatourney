from django.db import models

# Create your models here.
    
class Team(models.Model):
    Team_ID = models.IntegerField()
    Team_Name = models.CharField(max_length=30)
    Wins = models.IntegerField()
    Losses = models.IntegerField()
    Team_Rank = models.IntegerField()
    objects = models.Manager()

    def getTeam_ID(self):
        return self.Team_ID
    
    def getTeam_Name(self):
        return self.Team_Name
    
    def getWins(self):
        return self.Wins
    
    def getLosses(self):
        return self.Losses
    
    def getTeam_Rank(self):
        return self.Team_Rank
    
class Moderator(models.Model):
    moderator_username=models.CharField(max_length=20,primary_key=True)
    moderator_password=models.CharField
    moderator_lname=models.CharField(max_length=20)
    moderator_fname=models.CharField(max_length=20)
    objects = models.Manager()

    def getModeratorFullName(self):
        return f'{self.moderator_fname} {self.moderator_lname}'
    

    
class Player(models.Model):
    player_ID=models.AutoField(primary_key=True)
    player_in_game_name=models.CharField(max_length=20, blank=True, null=True)
    player_fname=models.CharField(max_length=20, blank=True, null=True)
    player_lname=models.CharField(max_length=20, blank=True, null=True)
    player_dc_id=models.CharField(max_length=15, blank=True, null=True)
    player_fc=models.CharField(max_length=14, blank=True, null=True)
    player_rank=models.CharField(max_length=5, blank=True, null=True)
    player_role=models.CharField(max_length=10, blank=True, null=True)
    player_type=models.CharField(max_length=10, default="member", null=True)
    player_checkin_status=models.CharField(max_length=20, blank=True, null=True)
    objects = models.Manager()
    Team_ID = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)    


    def getPlayer_ID(self):
        return self.player_ID
    
    def getPlayer_in_game_name(self):
        return self.player_in_game_name
    
    def getPlayerFullName(self):
        return f'{self.player_fname} {self.player_lname}'

    def getPlayerFirstName(self):
        return self.player_fname
    
    def getPlayerLastName(self):
        return self.player_lname
    
    def getPlayerDiscordID(self):
        return self.player_dc_id
    
    def getPlayerFriendCode(self):
        return self.player_fc
    
    def getPlayerRank(self):
        return self.player_rank
    
    def getPlayerRole(self):
        return self.player_role
    
    def getPlayerType(self):
        return self.player_type
    
    
    

