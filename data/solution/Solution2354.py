import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # Use a set to remove duplicates and then count the number of set bits for each unique number
        set_bits_count = Counter(map(lambda x: bin(x).count('1'), set(nums)))
        
        # Initialize the result
        result = 0
        
        # Iterate over all possible pairs of set bits counts
        for i in set_bits_count:
            for j in set_bits_count:
                if i + j >= k:
                    result += set_bits_count[i] * set_bits_count[j]
        
        return result

def countExcellentPairs(nums: List[int], k: int) -> int:
    return Solution().countExcellentPairs(nums, k)