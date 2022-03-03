import unittest
from city_functions import place_description

class TestPlaceDescription(unittest.TestCase):
    """test for city_functions.py"""
    def test_city_country(self):
        formatted_description = place_description("st petersburg", "russia")
        self.assertEqual(formatted_description, "St Petersburg, Russia")

    def test_city_country_population(self):
        formatted_description = place_description("moscow", "russia", "15kk")
        self.assertEqual(formatted_description, "Moscow, Russia - 15kk")

if __name__ == '__main__':
    unittest.main()

