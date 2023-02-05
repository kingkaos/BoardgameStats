from django.db import models
from django.utils.translation import gettext_lazy


class Boardgame(models.Model):

    class BoardgameType(models.TextChoices):
        COMPETITIVE = 'COMP', gettext_lazy('kompetitiv')
        COOPERATIVE = 'COOP', gettext_lazy('kooperativ')

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # type of game solitar, coop, compet
    type = models.CharField(
        max_length=4,
        choices=BoardgameType.choices,
        default=BoardgameType.COMPETITIVE
    )

    def __str__(self):
        return self.title
