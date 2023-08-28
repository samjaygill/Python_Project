import unittest

from models.destination import Destination

class TestDestination(unittest.TestCase):

    def setUp(self):
        self.destination = Destination("Paris", "France")

    def test_destination_has_city(self):
        self.assertEqual("Paris", self.destination.city)

    def test_destination_had_country(self):
        self.assertEqual("France", self.destination.country)