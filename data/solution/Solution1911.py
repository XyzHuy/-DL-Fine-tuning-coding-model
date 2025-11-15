import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Initialize two variables to keep track of the maximum alternating sum
        # ending with an even index and an odd index
        even_sum = 0
        odd_sum = 0
        
        for num in nums:
            # Update the even_sum to be the maximum of the previous even_sum
            # or the previous odd_sum plus the current number (indicating we
            # are adding this number to the subsequence at an even index)
            new_even_sum = max(even_sum, odd_sum + num)
            
            # Update the odd_sum to be the maximum of the previous odd_sum
            # or the previous even_sum minus the current number (indicating we
            # are adding this number to the subsequence at an odd index)
            odd_sum = max(odd_sum, even_sum - num)
            
            # Update the even_sum to the newly calculated value
            even_sum = new_even_sum
        
        # The result will be the maximum alternating sum ending at an even index
        return even_sum

def maxAlternatingSum(nums: List[int]) -> int:
    return Solution().maxAlternatingSum(nums)