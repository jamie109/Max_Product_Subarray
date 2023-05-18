
"""
@File ：main.py
@Author ：jamie109
@Date ：2023/5/18
"""

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

    def set_arr(self, arr_input):
        """
        get the array to cal
        :param arr_input:
        :return:
        """
        self.arr = arr_input
        self.lenth = len(arr_input)

        if self.lenth == 0:
            exit("blank array, exit")

        self.max_product = arr_input[0]
        self.cur_min = arr_input[0]
        self.cur_max = arr_input[0]
        print(f"set arr finish")

    def cal_max_pro(self):
        """
        cal max product
        :return:
        """
        for i in range(1, self.lenth):
            if self.arr[i] < 0:
                # exchange current max and min
                self.cur_max, self.cur_min = self.cur_min, self.cur_max
            # update current max and min
            self.cur_max = max(self.arr[i], self.cur_max * self.arr[i])
            self.cur_min = min(self.arr[i], self.cur_min * self.arr[i])
            # update max_product
            if self.max_product < self.cur_max:
                self.max_product = self.cur_max


def get_array():
    """
    get the array
    :return: array list
    """
    array_input = []
    try:
        array_input = eval(input("please input an array like [1,2,34]："))
    except SyntaxError:
        print("Syntax Error, input again")
    # 输入单词 汉字
    except NameError:
        print("NameError, please input an array")

    #print(type(array_input))
    return array_input



if __name__ == '__main__':
    # max_p, l = max_product_subarray([1, 0, -3, 2, -5])
    # print(max_p)
    # print(l)
    arr = get_array()
    max_pro = MaxProduct()
    max_pro.set_arr(arr)
    max_pro.cal_max_pro()
    print(f"the max product is {max_pro.max_product}")