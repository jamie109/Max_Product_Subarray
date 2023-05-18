"""
@File ：main.py
@Author ：jamie109
@Date ：2023/5/18
"""
import numpy as np


class MaxProduct:
    """
    cal the max product in subarrays
    """
    def __init__(self):
        self.max_product = 0
        self.cur_min = 0
        self.cur_max = 0
        self.arr = []
        self.lenth = 0
        # subarry index
        self.start_idx = 0
        self.end_idx = 0

    def set_arr(self, arr_input):
        """
        get the array to cal
        :param arr_input:the array to cal
        """
        self.arr = arr_input
        self.lenth = len(arr_input)

        if self.lenth == 0:
            exit("blank array, exit")

        self.max_product = arr_input[0]
        self.cur_min = arr_input[0]
        self.cur_max = arr_input[0]
        #print(f"set arr finish")

    def cal_max_pro(self):
        """
        cal max product
        """
        tmp_start = 0
        for i in range(1, self.lenth):
            if self.arr[i] < 0:
                # exchange current max and min
                self.cur_max, self.cur_min = self.cur_min, self.cur_max

            # update current max and min
            self.cur_max = max(self.arr[i], self.cur_max * self.arr[i])
            self.cur_min = min(self.arr[i], self.cur_min * self.arr[i])

            # update max_product and subarray index
            if self.max_product < self.cur_max:
                self.max_product = self.cur_max
                self.start_idx = tmp_start
                self.end_idx = i

            # meet 0 restart the subarray
            if self.cur_max == 0:
                tmp_start = i + 1


def get_array():
    """
    get the array
    :return: array list
    """
    array_input = []
    try:
        array_input = eval(input("please input an array like [-1,2,3,4]："))
        # 大于一维
        if len(np.array(array_input).shape) > 1:
            exit("Error, not a 1-D array")
    except SyntaxError:
        exit("Syntax Error, input again")
    # 输入单词 汉字
    except NameError:
        exit("NameError, please input an array")
    #print(type(array_input))
    return array_input


def read_array():
    """
    read data from txt
    :return: 2D list [arr1, arr2, arr3]
    """
    arrays = []
    with open('data.txt') as file:
        lines = file.readlines()
        for line in lines:
            cur_arr = line.split()
            cur_arr = [eval(item) for item in cur_arr]
            # print(cur_arr)
            # print(type(cur_arr))
            arrays.append(cur_arr)
    return arrays


if __name__ == '__main__':
    print("--------------------welcome---------------------")
    arr = get_array()
    max_pro = MaxProduct()
    max_pro.set_arr(arr)
    max_pro.cal_max_pro()
    print(f"the max product is {max_pro.max_product} and the subarray is"
          f" {arr[max_pro.start_idx : max_pro.end_idx + 1]}")

    # # read data from txt
    # arrs = read_array()
    # #print(arrs)
    # for arr in arrs:
    #     print(arr)
    #     max_pro = MaxProduct()
    #     max_pro.set_arr(arr)
    #     max_pro.cal_max_pro()
    #
    #     # if max_pro.start_idx == 0:
    #     #     start_index = max_pro.start_idx
    #     # else:
    #     #     start_index = max_pro.start_idx + 1
    #     # end_index = max_pro.end_idx + 1
    #
    #     print(f"the max product is {max_pro.max_product} and the subarray is"
    #   f" {arr[max_pro.start_idx: max_pro.end_idx + 1]}")