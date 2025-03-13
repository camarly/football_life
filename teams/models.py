from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)
    is_national_team = models.BooleanField(default=False)

    leagues = models.ManyToManyField('competitions.Competition', related_name="teams")
    last_performance = models.JSONField(default=dict, blank=True)  # Last season's performance
    current_standings = models.JSONField(default=dict, blank=True)  # Live competition standings
    silverware = models.IntegerField(default=0)  # Number of trophies won
    local_ranking = models.IntegerField(null=True, blank=True)  # Domestic ranking
    international_ranking = models.IntegerField(null=True, blank=True)  # FIFA/UEFA rankings

    crest_url = models.URLField(null=True, blank=True)
    market_value = models.FloatField(null=True, blank=True)  # Team value in millions

    def __str__(self):
        return self.name
