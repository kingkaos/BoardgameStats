from django.test import TestCase
from api.models.boardgame import Boardgame
from api.models.stats import Stats


class BoardgameTestCase(TestCase):
    def setUp(self):
        Boardgame.objects.create(title = "Azul")
        Boardgame.objects.create(
            title = "Andor",
            type = "COOP"
        )

    def test_type(self):
        azul = Boardgame.objects.get(title = "Azul")
        andor = Boardgame.objects.get(title = "Andor")

        self.assertEqual(azul.type, 'COMP')
        self.assertEqual(andor.type, 'COOP')


class StatsTestCase(TestCase):
    def setUp(self):
        Stats.objects.create()

    def test_create_data(self):
        print(Stats.objects.all()[0].played_on)
