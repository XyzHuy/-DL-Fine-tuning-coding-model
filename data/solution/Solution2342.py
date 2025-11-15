import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Dictionary to store the maximum number for each digit sum
        max_num_for_digit_sum = defaultdict(int)
        max_sum = -1
        
        for num in nums:
            # Calculate the sum of digits of the current number
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Check if we have seen this digit sum before
            if max_num_for_digit_sum[digit_sum] > 0:
                # Calculate the sum of the current number and the maximum number with the same digit sum
                max_sum = max(max_sum, num + max_num_for_digit_sum[digit_sum])
            
            # Update the maximum number for the current digit sum
            max_num_for_digit_sum[digit_sum] = max(max_num_for_digit_sum[digit_sum], num)
        
        return max_sum

def maximumSum(nums: List[int]) -> int:
    return Solution().maximumSum(nums)