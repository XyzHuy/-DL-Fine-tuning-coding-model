import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        # Step 1: Group indices by value
        value_to_indices = defaultdict(list)
        for i, value in enumerate(arr):
            value_to_indices[value].append(i)
        
        # Step 2: Initialize the result array
        n = len(arr)
        result = [0] * n
        
        # Step 3: Calculate prefix sums and distances for each group
        for indices in value_to_indices.values():
            # Calculate prefix sums for the group
            prefix_sum = [0]
            for index in indices:
                prefix_sum.append(prefix_sum[-1] + index)
            
            # Calculate the sum of distances for each index in the group
            for i, index in enumerate(indices):
                left_sum = i * index - prefix_sum[i]
                right_sum = prefix_sum[-1] - prefix_sum[i + 1] - (len(indices) - i - 1) * index
                result[index] = left_sum + right_sum
        
        return result

def getDistances(arr: List[int]) -> List[int]:
    return Solution().getDistances(arr)