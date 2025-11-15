import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = None
        maximum = None
        total_sum = 0
        total_count = 0
        mode = None
        max_count = 0
        
        # Calculate minimum, maximum, total_sum, total_count, and mode
        for i, c in enumerate(count):
            if c > 0:
                if minimum is None:
                    minimum = i
                maximum = i
                total_sum += i * c
                total_count += c
                if c > max_count:
                    max_count = c
                    mode = i
        
        # Calculate mean
        mean = total_sum / total_count
        
        # Calculate median
        def find_kth(k):
            cumulative_count = 0
            for i, c in enumerate(count):
                cumulative_count += c
                if cumulative_count >= k:
                    return i
        
        if total_count % 2 == 1:
            median = find_kth(total_count // 2 + 1)
        else:
            median = (find_kth(total_count // 2) + find_kth(total_count // 2 + 1)) / 2
        
        return [float(minimum), float(maximum), mean, median, float(mode)]

def sampleStats(count: List[int]) -> List[float]:
    return Solution().sampleStats(count)