import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        def count_pairs(freq):
            return sum(v * (v - 1) // 2 for v in freq.values())
        
        left = 0
        freq = defaultdict(int)
        current_pairs = 0
        result = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            current_pairs += freq[nums[right]] - 1
            
            while current_pairs >= k:
                result += len(nums) - right
                freq[nums[left]] -= 1
                current_pairs -= freq[nums[left]]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return result

def countGood(nums: List[int], k: int) -> int:
    return Solution().countGood(nums, k)