import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number in nums
        num_counts = Counter(nums)
        
        pairs = 0
        leftovers = 0
        
        # Iterate over the frequency of each number
        for count in num_counts.values():
            # Number of pairs that can be formed with this number
            pairs += count // 2
            # Number of leftovers after forming pairs
            leftovers += count % 2
        
        return [pairs, leftovers]

def numberOfPairs(nums: List[int]) -> List[int]:
    return Solution().numberOfPairs(nums)