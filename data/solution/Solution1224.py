import random
import functools
import collections
import string
import math
import datetime


from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = Counter()
        freq = Counter()
        max_len = 0
        
        for i, num in enumerate(nums):
            if num in count:
                freq[count[num]] -= 1
                if freq[count[num]] == 0:
                    del freq[count[num]]
            
            count[num] += 1
            freq[count[num]] += 1
            
            # Check conditions for valid prefix
            if len(freq) == 1:
                # All numbers have the same frequency
                key, value = next(iter(freq.items()))
                if key == 1 or value == 1:
                    max_len = i + 1
            
            elif len(freq) == 2:
                # There are exactly two different frequencies
                keys = list(freq.keys())
                values = list(freq.values())
                
                if (keys[0] == 1 and values[0] == 1) or (keys[1] == 1 and values[1] == 1):
                    # One of the frequencies is 1 and it appears only once
                    max_len = i + 1
                elif abs(keys[0] - keys[1]) == 1:
                    # Frequencies differ by 1
                    if (values[0] == 1 and keys[0] > keys[1]) or (values[1] == 1 and keys[1] > keys[0]):
                        max_len = i + 1
        
        return max_len

def maxEqualFreq(nums: List[int]) -> int:
    return Solution().maxEqualFreq(nums)