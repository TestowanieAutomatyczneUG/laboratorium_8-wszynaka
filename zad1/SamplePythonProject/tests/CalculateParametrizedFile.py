import unittest
from sample.Calculate import *


class CalculateParameterizedFile(unittest.TestCase):

    def test_from_file(self):
        fileTest = open("data/calculate_data_test")
        tmpCalc = Calculate()
        for line in fileTest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                a, b, result = int(data[0]), int(data[1]), int(data[2].strip("\n"))
                self.assertEqual(tmpCalc.dividingints(a, b), result)
        fileTest.close()


if __name__ == '__main__':
    unittest.main()
