import math
import unittest

from parameterized import parameterized, parameterized_class

from sample.Calculate import *


class CalculateParameterizedPackage(unittest.TestCase):

    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0),
        ("large fraction", 1.6, 1),
    ])
    def test_floor(self, name, input, expected):
        self.assertEqual(math.floor(input), expected)

    def setUp(self):
        self.tmp = Calculate()

    @parameterized.expand([
        (4, 2, 2),
        (3, 1, 3),
        (10, 2, 5),
    ])
    def test_one_parameterized(self, number1, number2, expected):
        self.assertEqual(self.tmp.dividingints(number1, number2), expected)


@parameterized_class(('number1', 'number2', 'expected'), [
    (4, 2, 2),
    (3, 1, 3),
    (10, 2, 5),
])
class CalculateParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Calculate()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.dividingints(self.number1, self.number2), self.expected)


if __name__ == '__main__':
    unittest.main()