def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # use set to check duplicate
    return len(nums) != len(set(nums))
