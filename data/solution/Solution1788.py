import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        # Dictionary to store the first and last occurrence of each beauty value
        first_occurrence = {}
        last_occurrence = {}
        prefix_sum = [0] * (len(flowers) + 1)
        
        # Calculate prefix sums and track first and last occurrences
        for i, beauty in enumerate(flowers):
            if beauty not in first_occurrence:
                first_occurrence[beauty] = i
            last_occurrence[beauty] = i
            prefix_sum[i + 1] = prefix_sum[i] + max(0, beauty)  # only add positive beauties to prefix sum
        
        max_beauty = float('-inf')
        
        # Calculate the maximum beauty of valid gardens
        for beauty in first_occurrence:
            start = first_occurrence[beauty]
            end = last_occurrence[beauty]
            if start != end:
                total_beauty = 2 * beauty + (prefix_sum[end] - prefix_sum[start + 1])
                max_beauty = max(max_beauty, total_beauty)
        
        return max_beauty

def maximumBeauty(flowers: List[int]) -> int:
    return Solution().maximumBeauty(flowers)