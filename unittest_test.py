"""
@File ：unittest_test.py
@Author ：jamie109
@Date ：2023/5/18
"""
import unittest
from maxpro import MaxProduct

class MaxProTest(unittest.TestCase):
    def test_cal1(self):
        maxpro = MaxProduct()
        maxpro.set_arr([1, 2, 3, 9])
        self.assertEqual(maxpro.cal_max_pro(), 54)

    def test_cal2(self):
        maxpro = MaxProduct()
        maxpro.set_arr([-3, -2, -19, -5, -1])
        self.assertEqual(maxpro.cal_max_pro(), 570)

    def test_cal3(self):
        maxpro = MaxProduct()
        maxpro.set_arr([-3, -2, -4, -5, -1, -6])
        self.assertEqual(maxpro.cal_max_pro(), 720)

    def test_cal4(self):
        maxpro = MaxProduct()
        maxpro.set_arr([0, 0, 0, 0, 0, 0])
        self.assertEqual(maxpro.cal_max_pro(), 0)

    def test_cal5(self):
        maxpro = MaxProduct()
        maxpro.set_arr([12, 9, 0, 8, 7, 4])
        self.assertEqual(maxpro.cal_max_pro(), 224)

    def test_cal6(self):
        maxpro = MaxProduct()
        maxpro.set_arr([-3, 0, -1, 0, -11, 0, -8, -3])
        self.assertEqual(maxpro.cal_max_pro(), 24)

    def test_cal7(self):
        maxpro = MaxProduct()
        maxpro.set_arr([3, -4, -11, 6, -2, 70, 6, 1])
        self.assertEqual(maxpro.cal_max_pro(), 55440)

    def test_cal8(self):
        maxpro = MaxProduct()
        maxpro.set_arr([0, 4, -6, 0, 2, -7, 9, -1, 8])
        self.assertEqual(maxpro.cal_max_pro(), 1008)


if __name__ == '__main__':
    unittest.main()
