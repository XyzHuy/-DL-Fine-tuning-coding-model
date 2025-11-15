import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def countSubarrays(nums, target):
            count = 0
            prefix_sums = defaultdict(int)
            prefix_sums[0] = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                count += prefix_sums[current_sum - target]
                prefix_sums[current_sum] += 1
            return count
        
        m, n = len(matrix), len(matrix[0])
        result = 0
        
        # Iterate over all possible pairs of rows
        for top in range(m):
            row_sums = [0] * n
            for bottom in range(top, m):
                # Update row_sums to include the current bottom row
                for col in range(n):
                    row_sums[col] += matrix[bottom][col]
                
                # Count the number of subarrays in row_sums that sum to target
                result += countSubarrays(row_sums, target)
        
        return result

def numSubmatrixSumTarget(matrix: List[List[int]], target: int) -> int:
    return Solution().numSubmatrixSumTarget(matrix, target)