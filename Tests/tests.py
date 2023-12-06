from django.test import TestCase

class SimpleTest(TestCase):
    def test_yes_equals_yes(self):
        self.assertEqual('yes', 'yes')