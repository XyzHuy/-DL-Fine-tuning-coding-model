import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Flatten the list of lists and count the occurrences of each number
        count = Counter(num for sublist in nums for num in sublist)
        
        # Find numbers that are present in every sublist
        result = [num for num, freq in count.items() if freq == len(nums)]
        
        # Return the result sorted in ascending order
        return sorted(result)

def intersection(nums: List[List[int]]) -> List[int]:
    return Solution().intersection(nums)