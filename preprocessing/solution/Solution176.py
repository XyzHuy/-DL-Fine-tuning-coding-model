def rob(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_helper(nums, 0, len(nums) - 2),
                rob_helper(nums, 1, len(nums) - 1))


def rob_helper(nums, low, high):
    prevMax = currMax = 0
    for index in range(low, high + 1):
        temp = currMax
        currMax = max(prevMax + nums[index], currMax)
        prevMax = temp
    return currMax