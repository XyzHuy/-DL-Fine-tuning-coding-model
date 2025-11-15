import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Count the frequency of each number in the array
        frequency = Counter(nums)
        operations = 0
        
        for count in frequency.values():
            # If any number appears only once, it's impossible to remove it
            if count == 1:
                return -1
            # Calculate the minimum number of operations needed for this count
            # We prioritize removing three elements at a time
            operations += (count // 3) + (1 if count % 3 != 0 else 0)
        
        return operations

def minOperations(nums: List[int]) -> int:
    return Solution().minOperations(nums)