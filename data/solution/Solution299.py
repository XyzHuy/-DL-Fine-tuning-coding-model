def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    broken_num = 0
    for i in range(len(nums) - 1):
        if (nums[i] > nums[i + 1]):
            broken_num += 1
            if broken_num >= 2:
                return False
            if (i - 1 < 0 or nums[i - 1] <= nums[i + 1]):
                # Remove i
                nums[i] = nums[i + 1]
            else:
                # Remove i + 1
                nums[i + 1] = nums[i]
    return True
