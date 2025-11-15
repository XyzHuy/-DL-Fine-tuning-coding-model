import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)
        count = [0] * (max_num + 1)
        
        # Count the occurrences of each number
        for num in nums:
            count[num] += 1
        
        # Create a prefix sum array
        prefix_sum = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix_sum[i] = prefix_sum[i - 1] + count[i]
        
        result = 0
        
        # Calculate the sum of floored pairs
        for x in range(1, max_num + 1):
            if count[x] == 0:
                continue
            for k in range(1, max_num // x + 1):
                right = min(k * x + x - 1, max_num)
                left = k * x
                multiples_count = prefix_sum[right] - prefix_sum[left - 1]
                result += k * multiples_count * count[x]
                result %= MOD
        
        return result

def sumOfFlooredPairs(nums: List[int]) -> int:
    return Solution().sumOfFlooredPairs(nums)