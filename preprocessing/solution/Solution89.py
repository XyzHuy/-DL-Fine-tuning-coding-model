def subsetsWithDup(nums):
    nums.sort()
    res = [[]]
    begin = 0
    for index in range(len(nums)):
        if index == 0 or nums[index] != nums[index - 1]:
            # generate all
            begin = 0
        size = len(res)
        # use existing subsets to generate new subsets
        for j in range(begin, size):
            curr = list(res[j])
            curr.append(nums[index])
            res.append(curr)
        # avoid duplicate subsets
        begin = size
    return res
