import random
import functools
import collections
import string
import math
import datetime


from typing import List
from sortedcontainers import SortedList

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left_counts = [0] * n
        right_counts = [0] * n
        
        # Counting for the left side
        left_sorted_list = SortedList()
        for i in range(n):
            left_counts[i] = left_sorted_list.bisect_left(nums[i])
            left_sorted_list.add(nums[i])
        
        # Counting for the right side
        right_sorted_list = SortedList()
        for i in range(n - 1, -1, -1):
            right_counts[i] = right_sorted_list.bisect_left(nums[i])
            right_sorted_list.add(nums[i])
        
        # Counting k-big indices
        k_big_indices_count = 0
        for i in range(n):
            if left_counts[i] >= k and right_counts[i] >= k:
                k_big_indices_count += 1
        
        return k_big_indices_count

def kBigIndices(nums: List[int], k: int) -> int:
    return Solution().kBigIndices(nums, k)