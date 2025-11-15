import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Count the occurrences of each number in nums2
        count_nums2 = Counter(nums2)
        
        # Calculate the total number of good pairs
        good_pairs = 0
        for num1 in nums1:
            for num2, count in count_nums2.items():
                if num1 % (num2 * k) == 0:
                    good_pairs += count
        
        return good_pairs

def numberOfPairs(nums1: List[int], nums2: List[int], k: int) -> int:
    return Solution().numberOfPairs(nums1, nums2, k)