import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # Calculate the length of the original array
        n = len(arr) + 1
        
        # Calculate the expected sum of the arithmetic progression
        expected_sum = (n * (arr[0] + arr[-1])) // 2
        
        # Calculate the actual sum of the given array
        actual_sum = sum(arr)
        
        # The missing number is the difference between the expected sum and the actual sum
        return expected_sum - actual_sum

def missingNumber(arr: List[int]) -> int:
    return Solution().missingNumber(arr)