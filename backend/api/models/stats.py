import uuid

from django.db import models

from .boardgame import Boardgame


class Stats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    played_on = models.DateField(auto_now_add=True)
    boardgame = models.ForeignKey('Boardgame', on_delete=models.CASCADE, null=True)

