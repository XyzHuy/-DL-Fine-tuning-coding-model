import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # Sort the numbers in non-increasing order
        nums.sort(reverse=True)
        
        total_sum = sum(nums)
        subsequence_sum = 0
        subsequence = []
        
        # Iterate through the sorted numbers and add to subsequence
        for num in nums:
            subsequence.append(num)
            subsequence_sum += num
            # Check if the subsequence sum is greater than the remaining sum
            if subsequence_sum > total_sum - subsequence_sum:
                break
        
        return subsequence

def minSubsequence(nums: List[int]) -> List[int]:
    return Solution().minSubsequence(nums)