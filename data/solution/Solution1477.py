import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + arr[i]
        
        min_lengths = [float('inf')] * (n + 1)
        result = float('inf')
        left = 0
        
        for right in range(n + 1):
            while prefix_sums[right] - prefix_sums[left] > target:
                left += 1
            
            if prefix_sums[right] - prefix_sums[left] == target:
                current_length = right - left
                if min_lengths[left] < float('inf'):
                    result = min(result, current_length + min_lengths[left])
                min_lengths[right] = min(min_lengths[right - 1], current_length)
            else:
                min_lengths[right] = min_lengths[right - 1]
        
        return result if result < float('inf') else -1

def minSumOfLengths(arr: List[int], target: int) -> int:
    return Solution().minSumOfLengths(arr, target)