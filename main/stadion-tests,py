from unittest import TestCase
from stadion.models import Anlage
from stadion.models import Stadion


class AnlagenTests(TestCase):
    def test_defaults(self):
        anlage = Anlage()
        self.assertEqual(anlage.id, None)
        self.assertEqual(anlage.bezeichnung, "")
        self.assertEqual(anlage.homologiert, "y")
        self.assertEqual(anlage.stadion_id, None)
        #self.assertEqual(anlage.stadion, None)

    def test_bezeichnung(self):
        bezeichnung = "UMM"
        anlage = Anlage(bezeichnung=bezeichnung)
        self.assertEqual(anlage.bezeichnung, bezeichnung)


class StadionTests(TestCase):
    def test_defaults(self):
        stadion = Stadion()
        self.assertEqual(stadion.id, None)
        self.assertEqual(stadion.name, "")
        self.assertEqual(stadion.bahnen, 6)
        self.assertEqual(stadion.bahnengerade, 6)
        self.assertEqual(stadion.halle, "n")
        self.assertEqual(stadion.ueber1000m, "n")
        self.assertEqual(stadion.anlagen.count(), 0)

    def test_object_save_and_get(self):
        stadion = Stadion(name="Buchholz")
        stadion.save()
        stadion_id = stadion.id
        self.assertNotEqual(stadion_id, None)
        Stadion.objects.get(id=stadion_id)

    def test_object_create_and_get(self):
        stadion = Stadion.objects.create()
        stadion_id = stadion.id
        self.assertNotEqual(stadion_id, None)
        Stadion.objects.get(id=stadion_id)

    def test_stadion_anlage_relation(self):
        stadion = Stadion.objects.create(name="Buchholz")
        self.assertEqual(stadion.anlagen.count(), 0)

        bezeichnung = "Hochsprung"
        stadion.anlagen.create(bezeichnung=bezeichnung)
        self.assertEqual(stadion.anlagen.count(), 1)
        self.assertEqual(stadion.anlagen.first().bezeichnung, bezeichnung)

        anlage = Anlage(bezeichnung="Weitsprung")
        stadion.anlagen.add(anlage)
        self.assertEqual(stadion, anlage.stadion)
        self.assertEqual(stadion.anlagen.count(), 2)
        self.assertIn(anlage, list(stadion.anlagen.all()))
