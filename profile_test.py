"""
@File ：profile_test.py
@Author ：jamie109
@Date ：2023/5/18
"""
import profile
import numpy as np
from maxpro import get_array, MaxProduct


def fun_run(array):
    #arr = get_array()
    max_pro = MaxProduct()
    max_pro.set_arr(array)
    max_pro.cal_max_pro()


if __name__ == '__main__':
    arr = [np.random.randint(-1000, 1000) for i in range(100000)]
    print("random arr finish")
    profile.run("fun_run(arr)")