# Generated by Django 5.0.3 on 2024-05-07 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SplatourneyApp', '0003_alter_player_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Team_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.team'),
        ),
    ]