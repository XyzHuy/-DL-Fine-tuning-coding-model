import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count the frequency of each element in the array
        frequency = Counter(nums)
        
        # Find the maximum frequency
        max_freq = max(frequency.values())
        
        # Calculate the total number of elements with the maximum frequency
        total_max_freq_elements = sum(count for count in frequency.values() if count == max_freq)
        
        return total_max_freq_elements

def maxFrequencyElements(nums: List[int]) -> int:
    return Solution().maxFrequencyElements(nums)