import uuid

from django.db import models
from django.utils.translation import gettext_lazy


class Boardgame(models.Model):

    class BoardgameType(models.TextChoices):
        COMPETITIVE = 'COMP', gettext_lazy('kompetitiv')
        COOPERATIVE = 'COOP', gettext_lazy('kooperativ')

    class BoardgameKind(models.TextChoices):
        STANDARD = 'STD', gettext_lazy('')
        FAMILY = 'FAM', gettext_lazy('Familie')
        KIDS = 'KID', gettext_lazy('Kinder')
        ADULT = 'ADU', gettext_lazy('Erwachsene')
        EXPERT = 'EXP', gettext_lazy('Experten')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_expansion = models.BooleanField(default=False)
    # basegame = models.ForeignKey('self', on_delete=models.CASCADE)

    min_player = models.PositiveSmallIntegerField(blank=True, null=True)
    max_player = models.PositiveSmallIntegerField(blank=True, null=True)

    min_duration = models.PositiveSmallIntegerField(blank=True, null=True)
    max_duration = models.PositiveSmallIntegerField(blank=True, null=True)
    # game_variants = models.JSONField(null=True)
    # type of game coop or comp
    type = models.CharField(
        max_length=4,
        choices=BoardgameType.choices,
        default=BoardgameType.COMPETITIVE
    )
    kind = models.CharField(
        max_length=3,
        choices=BoardgameKind.choices,
        default=BoardgameKind.STANDARD
    )

    def __str__(self):
        return f"{self.title} {self.type}"
