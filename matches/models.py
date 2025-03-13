from django.db import models

class Match(models.Model):
    competition = models.ForeignKey('competitions.Competition', on_delete=models.CASCADE)
    matchday = models.IntegerField()

    home_team = models.ForeignKey('teams.Team', related_name="home_matches", on_delete=models.CASCADE)
    away_team = models.ForeignKey('teams.Team', related_name="away_matches", on_delete=models.CASCADE)

    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('UPCOMING', 'Upcoming'),
        ('ONGOING', 'Ongoing'),
        ('FINISHED', 'Finished')
    ])

    full_time_score = models.JSONField(null=True, blank=True)  # {"home": 2, "away": 1}
    half_time_score = models.JSONField(null=True, blank=True)
    match_events = models.JSONField(null=True, blank=True)  # Stores events like goals, cards, substitutions

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.competition}"
