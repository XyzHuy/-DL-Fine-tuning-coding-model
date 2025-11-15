import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Count the frequency of each number in the array
        freq = Counter(arr)
        
        # Sort the frequencies in descending order
        sorted_freq = sorted(freq.values(), reverse=True)
        
        half_size = len(arr) // 2
        current_size = len(arr)
        set_size = 0
        
        # Remove elements until the current size is less than or equal to half the original size
        for count in sorted_freq:
            set_size += 1
            current_size -= count
            if current_size <= half_size:
                return set_size

def minSetSize(arr: List[int]) -> int:
    return Solution().minSetSize(arr)