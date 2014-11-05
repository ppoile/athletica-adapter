from django.test import TestCase
from stadion.models import Anlage
from stadion.models import Stadion

class AnlagenTests(TestCase):
    def test_defaults(self):
        anlage = Anlage()
        self.assertEqual(anlage.id, None)
        self.assertEqual(anlage.bezeichnung, "")
        self.assertEqual(anlage.homologiert, "y")
        self.assertEqual(anlage.stadion_id, None)

    def test_bezeichnung(self):
        bezeichnung = "UMM"
        anlage = Anlage(bezeichnung=bezeichnung)
        self.assertEqual(anlage.bezeichnung, bezeichnung)


class StadionTests(TestCase):
    def test_defaults(self):
        stadion = Stadion()
        self.assertEqual(stadion.id, None)
        self.assertEqual(stadion.name, "")
        self.assertEqual(stadion.bahnen, None)
        self.assertEqual(stadion.bahnengerade, None)
        self.assertEqual(stadion.halle, "n")
        self.assertEqual(stadion.ueber1000m, "n")

    def test_object_creation(self):
        stadion = Stadion.objects.create(name="Buchholz")

    def test_stadion_anlage_relation(self):
        anlage = Anlage()
        stadion = Stadion()
        anlage.stadion = stadion
        self.assertEqual(anlage.stadion_id, stadion.id)
