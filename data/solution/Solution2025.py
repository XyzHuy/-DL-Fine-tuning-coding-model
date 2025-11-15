import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        count = 0
        left_diffs = defaultdict(int)
        right_diffs = defaultdict(int)

        # Calculate initial number of partitions without any change
        for i in range(n - 1):
            prefix_sum += nums[i]
            if prefix_sum == (total_sum - prefix_sum):
                count += 1
            right_diffs[prefix_sum - (total_sum - prefix_sum)] += 1

        max_ways = count

        # Try changing each element to k and calculate the number of partitions
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            # If we change nums[i] to k, the difference changes by (k - nums[i])
            diff = k - nums[i]
            # Number of ways if we change nums[i] to k
            ways = left_diffs[diff] + right_diffs[-diff]
            max_ways = max(max_ways, ways)
            # Update the left and right differences
            left_diffs[prefix_sum - (total_sum - prefix_sum)] += 1
            right_diffs[prefix_sum - (total_sum - prefix_sum)] -= 1

        return max_ways

def waysToPartition(nums: List[int], k: int) -> int:
    return Solution().waysToPartition(nums, k)