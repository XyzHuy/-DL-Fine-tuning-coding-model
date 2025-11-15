import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        # Separate the numbers into even and odd lists
        evens = [num for num in nums if num % 2 == 0]
        odds = [num for num in nums if num % 2 != 0]
        
        # Sort both lists in descending order
        evens.sort(reverse=True)
        odds.sort(reverse=True)
        
        # Function to get the sum of the first n elements of a list
        def prefix_sum(lst, n):
            return sum(lst[:n])
        
        max_sum = -1
        
        # Try to form a subsequence of length k with the largest even sum
        for i in range(0, k + 1, 2):  # i is the number of odds we take
            if i > len(odds) or (k - i) > len(evens):
                continue
            current_sum = prefix_sum(odds, i) + prefix_sum(evens, k - i)
            if current_sum % 2 == 0:
                max_sum = max(max_sum, current_sum)
        
        return max_sum

def largestEvenSum(nums: List[int], k: int) -> int:
    return Solution().largestEvenSum(nums, k)