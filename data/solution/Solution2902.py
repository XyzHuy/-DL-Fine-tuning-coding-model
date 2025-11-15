import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

MOD = 10**9 + 7

class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        # Count the frequency of each number in nums
        count = Counter(nums)
        unique_nums = list(count.keys())
        n = len(unique_nums)
        
        # Handle the special case where 0 is in the array
        zero_count = count[0]
        if 0 in count:
            del count[0]
            unique_nums.remove(0)
        
        # Initialize the DP array
        dp = [0] * (r + 1)
        dp[0] = 1  # The empty sub-multiset
        
        # Iterate over each unique number
        for num in unique_nums:
            # Create a new DP array to store the results for this iteration
            new_dp = dp[:]
            freq = count[num]
            for target in range(1, r + 1):
                # Calculate the maximum number of times we can take this number
                max_times = min(freq, target // num)
                for times in range(1, max_times + 1):
                    if target - num * times >= 0:
                        new_dp[target] = (new_dp[target] + dp[target - num * times]) % MOD
            dp = new_dp
        
        # Sum up all the valid sub-multisets
        result = sum(dp[l:r + 1]) % MOD
        
        # If there are zeros, we can add any number of zeros to any valid sub-multiset
        if zero_count > 0:
            result = (result * (zero_count + 1)) % MOD
        
        return result

def countSubMultisets(nums: List[int], l: int, r: int) -> int:
    return Solution().countSubMultisets(nums, l, r)