import unittest

class TestCelsiusToKelvin(unittest.TestCase):

    def test_freezing_point(self):
        self.assertEqual(celsius_to_kelvin(0), 273.15)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_kelvin(100), 373.15)

    def test_negative_temperature(self):
        self.assertEqual(celsius_to_kelvin(-273.15), 0)

    def test_decimal_temperature(self):
        self.assertAlmostEqual(celsius_to_kelvin(25.5), 298.65, places=2)

    def test_large_temperature(self):
        self.assertEqual(celsius_to_kelvin(1000), 1273.15)

if _name_ == '_main_':
        unittest.main()