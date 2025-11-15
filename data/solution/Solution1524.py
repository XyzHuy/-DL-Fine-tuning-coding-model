import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        prefix_sum = 0
        odd_count = 0
        even_count = 1  # Starting with 1 because the prefix sum of 0 is considered even
        result = 0
        
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                # If current prefix sum is even, then the number of odd subarrays ending here
                # is equal to the number of times we have seen an odd prefix sum
                result += odd_count
                even_count += 1
            else:
                # If current prefix sum is odd, then the number of odd subarrays ending here
                # is equal to the number of times we have seen an even prefix sum
                result += even_count
                odd_count += 1
        
        return result % MOD

def numOfSubarrays(arr: List[int]) -> int:
    return Solution().numOfSubarrays(arr)