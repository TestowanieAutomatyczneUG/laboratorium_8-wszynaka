import unittest
from zad3.Calculate import Calculate


class CalcualteTest(unittest.TestCase):

    def setUp(self):
        self.temp = Calculate()

    def test1(self):
        self.assertEqual(self.temp.dividingints(2, 1), 2)

    def test2(self):
        self.assertEqual(self.temp.dividingints(4, 2), 2)

    def test3(self):
        self.assertEqual(self.temp.dividingints(4, 1), 4)

    def test4(self):
        self.assertEqual(self.temp.dividingints(50, 25), 2)

    def test5(self):
        self.assertEqual(self.temp.dividingints(200, 100), 2)

    def test6(self):
        self.assertEqual(self.temp.dividingints(52, 2), 26)

    def test7(self):
        self.assertEqual(self.temp.dividingints(-13, 13), -1)

    def test8(self):
        self.assertEqual(self.temp.dividingints(-33, -3), 11)

    def test_not_ints(self):
        self.assertRaises(Exception, self.temp.dividingints, 1.5, 1.8)

    def test_not_ints2(self):
        self.assertRaises(Exception, self.temp.dividingints, -3.5, -18)

    def tearDown(self):
        self.temp = None
