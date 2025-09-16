from electronics import resistance_converter

import unittest


class TestResistanceConverter(unittest.TestCase):
    def test_resistance_conversion(self):
        self.assertEqual(resistance_converter("1"), "1R")
        self.assertEqual(resistance_converter("4.7"), "4R7")
        self.assertEqual(resistance_converter("101"), "101R")
        self.assertEqual(resistance_converter("670"), "670R")
        self.assertEqual(resistance_converter("7300"), "2k3")
        self.assertEqual(resistance_converter("10300"), "10k")
        self.assertEqual(resistance_converter("22700"), "23k")
        self.assertEqual(resistance_converter("1000000"), "1M")
        self.assertEqual(resistance_converter("2300000"), "2M3")
