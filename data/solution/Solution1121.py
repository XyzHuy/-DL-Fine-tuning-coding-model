import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        # Count the frequency of each number in the sorted array
        freq = Counter(nums)
        
        # Find the maximum frequency of any number
        max_freq = max(freq.values())
        
        # To divide the array into subsequences of length at least k,
        # the number of subsequences needed is at least max_freq.
        # And each of these subsequences must be of length at least k.
        # Therefore, the total length of the array must be at least max_freq * k.
        return len(nums) >= max_freq * k

def canDivideIntoSubsequences(nums: List[int], k: int) -> bool:
    return Solution().canDivideIntoSubsequences(nums, k)