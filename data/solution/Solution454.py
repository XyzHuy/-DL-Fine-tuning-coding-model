import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Create a dictionary to store the sum of pairs from nums1 and nums2
        sum_ab = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_ab[a + b] += 1
        
        # Count the number of tuples that sum to zero
        count = 0
        for c in nums3:
            for d in nums4:
                if -(c + d) in sum_ab:
                    count += sum_ab[-(c + d)]
        
        return count

def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    return Solution().fourSumCount(nums1, nums2, nums3, nums4)