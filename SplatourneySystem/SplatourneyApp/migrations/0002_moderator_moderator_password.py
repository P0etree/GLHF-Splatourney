# Generated by Django 5.0.3 on 2024-04-04 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SplatourneyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moderator',
            name='moderator_password',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]