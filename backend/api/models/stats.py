from django.db import models
from .boardgame import Boardgame


class Stats(models.Model):

    played_on = models.DateField(auto_now_add=True)
    boardgame = models.ForeignKey('Boardgame', on_delete=models.CASCADE, null=True)

