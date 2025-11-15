import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of prefix sums modulo k
        prefix_mod_count = defaultdict(int)
        prefix_mod_count[0] = 1  # Initialize with 0 to handle subarrays that are exactly divisible by k
        
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            # Calculate the modulo of the current prefix sum with k
            mod = prefix_sum % k
            # Adjust mod to be positive if it's negative
            if mod < 0:
                mod += k
            # If this modulo has been seen before, it means there are subarrays ending at the current index
            # which are divisible by k
            if mod in prefix_mod_count:
                count += prefix_mod_count[mod]
            # Increment the count of this modulo in the dictionary
            prefix_mod_count[mod] += 1
        
        return count

def subarraysDivByK(nums: List[int], k: int) -> int:
    return Solution().subarraysDivByK(nums, k)