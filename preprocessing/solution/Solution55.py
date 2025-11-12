def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # greedy
    length = len(nums)
    begin = length - 1
    for i in reversed(range(length - 1)):
        if i + nums[i] >= begin:
            begin = i
    return not begin
