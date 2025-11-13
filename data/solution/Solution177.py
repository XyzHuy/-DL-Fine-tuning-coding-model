def findKthLargest(nums, k):
    import random
    # shuffle nums to avoid n*n
    random.shuffle(nums)
    return quickSelection(nums, 0, len(nums) - 1, len(nums) - k)

def quickSelection(nums, start, end, k):
    if start > end:
        return float('inf')
    pivot = nums[end]
    left = start
    for i in range(start, end):
        if nums[i] <= pivot:
            # swip left and i
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
    nums[left], nums[end] = nums[end], nums[left]
    if left == k:
        return nums[left]
    elif left < k:
        return quickSelection(nums, left + 1, end, k)
    else:
        return quickSelection(nums, start, left - 1, k)
