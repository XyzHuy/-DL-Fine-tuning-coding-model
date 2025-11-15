import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            # Calculate the number of subarrays in which arr[i] is included
            # (i + 1) choices for the start of the subarray
            # (n - i) choices for the end of the subarray
            # (i + 1) * (n - i) is the total number of subarrays including arr[i]
            # Half of these will be odd length
            count_subarrays = (i + 1) * (n - i)
            odd_count = (count_subarrays + 1) // 2
            
            total_sum += arr[i] * odd_count
        
        return total_sum

def sumOddLengthSubarrays(arr: List[int]) -> int:
    return Solution().sumOddLengthSubarrays(arr)