import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        total_cost = 0
        same_value_indices = []
        
        # Collect indices where nums1[i] == nums2[i]
        for i in range(n):
            if nums1[i] == nums2[i]:
                same_value_indices.append(i)
                total_cost += i
        
        if not same_value_indices:
            return 0
        
        # Count the frequency of the most common value among the same_value_indices
        count = Counter(nums1[i] for i in same_value_indices)
        most_common_value, most_common_count = count.most_common(1)[0]
        
        # If the most common value appears more than half the time, we need extra swaps
        if most_common_count * 2 > len(same_value_indices):
            # We need to find additional swaps to balance out
            extra_needed = most_common_count - (len(same_value_indices) - most_common_count)
            for i in range(n):
                if i not in same_value_indices and nums1[i] != most_common_value and nums2[i] != most_common_value:
                    total_cost += i
                    extra_needed -= 1
                    if extra_needed == 0:
                        break
            
            if extra_needed > 0:
                return -1
        
        return total_cost

def minimumTotalCost(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minimumTotalCost(nums1, nums2)