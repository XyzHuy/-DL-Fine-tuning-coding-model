def sum_of_two_largest(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return largest + second_largest
