from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=100, unique=True)
    competition_type = models.CharField(max_length=50, choices=[
        ('League', 'League'),
        ('Cup', 'Cup'),
        ('International', 'International')
    ])
    region = models.CharField(max_length=100)
    season_year = models.IntegerField()

    current_matchday = models.IntegerField(null=True, blank=True)
    number_of_matchdays = models.IntegerField(null=True, blank=True)
    number_of_teams = models.IntegerField(null=True, blank=True)
    number_of_games = models.IntegerField(null=True, blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.season_year})"
