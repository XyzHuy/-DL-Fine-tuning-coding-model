import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict
        
        # Dictionary to store the frequency of prefix sums
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case: a prefix sum of 0 occurs once at the start
        
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - goal) exists in the dictionary, it means there is a subarray ending at the current index
            # which sums up to the goal
            if (current_sum - goal) in prefix_sum_count:
                result += prefix_sum_count[current_sum - goal]
            
            # Update the frequency of the current prefix sum
            prefix_sum_count[current_sum] += 1
        
        return result

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    return Solution().numSubarraysWithSum(nums, goal)