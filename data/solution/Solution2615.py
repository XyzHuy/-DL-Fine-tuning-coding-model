import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Dictionary to store the indices of each number
        index_map = defaultdict(list)
        
        # Populate the dictionary with indices
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        # Result array initialized to 0
        arr = [0] * len(nums)
        
        # Calculate the sum of distances for each number
        for indices in index_map.values():
            n = len(indices)
            if n == 1:
                continue
            
            # Prefix sum of indices
            prefix_sum = [0] * n
            prefix_sum[0] = indices[0]
            for i in range(1, n):
                prefix_sum[i] = prefix_sum[i - 1] + indices[i]
            
            # Suffix sum of indices
            suffix_sum = [0] * n
            suffix_sum[-1] = indices[-1]
            for i in range(n - 2, -1, -1):
                suffix_sum[i] = suffix_sum[i + 1] + indices[i]
            
            # Calculate the distance for each index
            for i in range(n):
                left_distance = i * indices[i] - prefix_sum[i]
                right_distance = suffix_sum[i] - (n - i - 1) * indices[i]
                arr[indices[i]] = left_distance + right_distance
        
        return arr

def distance(nums: List[int]) -> List[int]:
    return Solution().distance(nums)