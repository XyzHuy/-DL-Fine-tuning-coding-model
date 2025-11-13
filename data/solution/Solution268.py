def canPartition(nums):
    total_sum = sum(nums)
    if total_sum & 1:
        return False
    # if sum of some elements can be half of total sum then true
    target = total_sum >> 1
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] | dp[i - num]
    return dp[target] == 1
