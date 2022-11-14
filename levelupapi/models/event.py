from django.db import models


class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='event_game', null=True, blank=True)
    description = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    time = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='event_organizer',null=True, blank=True)


