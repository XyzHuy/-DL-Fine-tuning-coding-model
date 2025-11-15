import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Filter out even numbers
        even_nums = [num for num in nums if num % 2 == 0]
        
        # If there are no even numbers, return -1
        if not even_nums:
            return -1
        
        # Count the frequency of each even number
        frequency = Counter(even_nums)
        
        # Find the most frequent even number, with a tie-breaker of the smallest number
        most_frequent = min(frequency, key=lambda x: (-frequency[x], x))
        
        return most_frequent

def mostFrequentEven(nums: List[int]) -> int:
    return Solution().mostFrequentEven(nums)