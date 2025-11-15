import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number in the list
        frequency = Counter(nums)
        
        # Sort the numbers first by frequency (ascending) then by the number itself (descending)
        sorted_nums = sorted(nums, key=lambda x: (frequency[x], -x))
        
        return sorted_nums

def frequencySort(nums: List[int]) -> List[int]:
    return Solution().frequencySort(nums)