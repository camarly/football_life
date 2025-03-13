from django.db import models

class Coach(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    experience_years = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    positions = models.JSONField()  # List of positions
    shirt_number = models.IntegerField(null=True, blank=True)
    current_team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, blank=True)
    contract_start = models.DateField(null=True, blank=True)
    contract_end = models.DateField(null=True, blank=True)

    # Key stats
    goals = models.FloatField(default=0.0)  # Goals per 90 minutes
    assists = models.FloatField(default=0.0)  # Assists per 90 minutes
    expected_goals = models.FloatField(null=True, blank=True)  # xG
    expected_assists = models.FloatField(null=True, blank=True)  # xA
    shots_attempted = models.FloatField(default=0.0)
    shots_on_target = models.FloatField(default=0.0)
    shot_accuracy = models.FloatField(null=True, blank=True)  # Percentage
    goals_per_shot = models.FloatField(null=True, blank=True)
    goals_per_shot_on_target = models.FloatField(null=True, blank=True)
    shots_from_free_kicks = models.FloatField(default=0.0)

    # Passing & Playmaking
    pass_completion = models.FloatField(null=True, blank=True)  # Pass completion %
    progressive_passes = models.FloatField(default=0.0)
    passes_into_final_third = models.FloatField(default=0.0)
    passes_into_penalty_area = models.FloatField(default=0.0)
    crosses_into_penalty_area = models.FloatField(default=0.0)
    through_balls = models.FloatField(default=0.0)
    corner_kicks = models.FloatField(default=0.0)

    # Defensive Stats
    tackles_attempted = models.FloatField(default=0.0)
    tackles_won = models.FloatField(default=0.0)
    tackles_def_3rd = models.FloatField(default=0.0)  # Defensive third
    tackles_mid_3rd = models.FloatField(default=0.0)  # Midfield third
    tackles_att_3rd = models.FloatField(default=0.0)  # Attacking third
    dribblers_tackled = models.FloatField(default=0.0)
    dribbles_challenged = models.FloatField(default=0.0)
    dribble_success_rate = models.FloatField(null=True, blank=True)  # %
    interceptions = models.FloatField(default=0.0)
    blocks = models.FloatField(default=0.0)
    passes_blocked = models.FloatField(default=0.0)
    clearances = models.FloatField(default=0.0)
    errors_leading_to_goals = models.FloatField(default=0.0)

    # Possession & Dribbling
    touches = models.FloatField(default=0.0)  # Total touches per 90
    touches_def_3rd = models.FloatField(default=0.0)
    touches_mid_3rd = models.FloatField(default=0.0)
    touches_att_3rd = models.FloatField(default=0.0)
    successful_take_ons = models.FloatField(default=0.0)
    take_on_success_rate = models.FloatField(null=True, blank=True)  # %
    carries = models.FloatField(default=0.0)
    progressive_carrying_distance = models.FloatField(default=0.0)
    miscontrols = models.FloatField(default=0.0)
    dispossessions = models.FloatField(default=0.0)

    # Miscellaneous Stats
    fouls_committed = models.FloatField(default=0.0)
    fouls_drawn = models.FloatField(default=0.0)
    offsides = models.FloatField(default=0.0)
    aerial_duels_won = models.FloatField(default=0.0)
    aerial_duels_lost = models.FloatField(default=0.0)
    aerial_win_rate = models.FloatField(null=True, blank=True)  # %
    own_goals = models.FloatField(default=0.0)
    penalty_kicks_won = models.FloatField(default=0.0)
    penalty_kicks_conceded = models.FloatField(default=0.0)

    # Additional Data Fields
    tendencies = models.JSONField(null=True, blank=True)  # e.g., {"hot_head": True, "loyal": False}
    trophies = models.JSONField(null=True, blank=True)  # List of trophies and awards
    market_value = models.FloatField(null=True, blank=True)  # Market value (in millions)
    is_free_agent = models.BooleanField(default=False)  # Whether the player is a free agent

    # Linking to Coaches
    coaches = models.ManyToManyField('Coach', related_name='players')

    def __str__(self):
        return f"{self.name} ({self.nationality})"
from django.db import models

# Create your models here.
