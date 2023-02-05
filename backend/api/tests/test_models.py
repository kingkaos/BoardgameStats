from django.test import TestCase
from api.models.boardgame import Boardgame

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
