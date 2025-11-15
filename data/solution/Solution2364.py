import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the total number of pairs
        total_pairs = n * (n - 1) // 2
        
        # Calculate the value of nums[i] - i for each i
        differences = [nums[i] - i for i in range(n)]
        
        # Count the occurrences of each difference
        count = Counter(differences)
        
        # Calculate the number of good pairs
        good_pairs = 0
        for freq in count.values():
            good_pairs += freq * (freq - 1) // 2
        
        # The number of bad pairs is the total pairs minus the good pairs
        return total_pairs - good_pairs

def countBadPairs(nums: List[int]) -> int:
    return Solution().countBadPairs(nums)