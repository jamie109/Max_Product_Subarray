def max_product_subarray(nums):
    if not nums:
        return 0, []

    max_product = nums[0]
    current_max = nums[0]
    current_min = nums[0]
    max_start = 0
    max_end = 0
    start = 0

    for i in range(1, len(nums)):
        if nums[i] < 0:
            # 交换当前最大值和最小值
            current_max, current_min = current_min, current_max

        # 更新当前最大值和最小值
        current_max = max(nums[i], current_max * nums[i])
        current_min = min(nums[i], current_min * nums[i])

        # 更新全局最大乘积及子数组的起始和结束位置
        if current_max > max_product:
            max_product = current_max
            max_start = start
            max_end = i

        # 如果当前最大乘积变为0，重置起始位置
        if current_max == 0:
            start = i + 1

    return max_product, nums[max_start - 1:max_end+1]


if __name__ == '__main__':
    max_p, l = max_product_subarray([1, 0, -3, 2, -5])
    print(max_p)
    print(l)