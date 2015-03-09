from django.test import TestCase

class MeetingTestCase(TestCase):
    fixtures = ['umm_2014_before.json']

    def setUp(self):
	pass

    def test1(self):
        import pdb; pdb.set_trace()
