def searchInsert(nums, target):
    l, r = int(0), len(nums) - 1
    while l < r:
        mid = int((l + r) / 2)
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    if nums[l] < target:
        return l + 1
    return l
