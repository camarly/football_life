from django.db import models

class Transfer(models.Model):
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)
    from_team = models.ForeignKey('teams.Team', related_name="outgoing_transfers", null=True, blank=True, on_delete=models.SET_NULL)
    to_team = models.ForeignKey('teams.Team', related_name="incoming_transfers", null=True, blank=True, on_delete=models.SET_NULL)

    transfer_date = models.DateField()
    transfer_fee = models.FloatField(null=True, blank=True)
    contract_length = models.IntegerField(null=True, blank=True)  # Length of contract in years

    is_loan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.name} -> {self.to_team.name if self.to_team else 'Free Agent'}"
