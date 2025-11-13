def threeSumSmaller(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    ls = len(nums)
    res = 0
    for i in range(ls - 1):
        res += twoSumSmaller(nums, i + 1, target - nums[i])
    return res

def twoSumSmaller(nums, start, target):
    res, left, right = 0, start, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            res += right - left
            left += 1
        else:
            right -= 1
    return res