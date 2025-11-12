def containsNearbyDuplicate(nums, k):
    # check k interval
    check = set()
    for i in range(len(nums)):
        if i > k:
            check.remove(nums[i - k - 1])
        if nums[i] in check:
            return True
        else:
            check.add(nums[i])
    return False
