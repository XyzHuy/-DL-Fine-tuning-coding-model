import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        for top in range(m):
            row_sums = [0] * n
            for bottom in range(top, m):
                for col in range(n):
                    row_sums[col] += matrix[bottom][col]
                
                # Now we need to find the max subarray sum no larger than k
                # Using prefix sum and binary search
                curr_sum, prefix_sums = 0, [0]
                for num in row_sums:
                    curr_sum += num
                    # We want to find the smallest prefix sum such that curr_sum - prefix_sum <= k
                    # This is equivalent to finding the smallest prefix_sum such that prefix_sum >= curr_sum - k
                    idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, curr_sum - prefix_sums[idx])
                    # Insert the current prefix sum into the sorted list
                    bisect.insort(prefix_sums, curr_sum)
        
        return max_sum

def maxSumSubmatrix(matrix: List[List[int]], k: int) -> int:
    return Solution().maxSumSubmatrix(matrix, k)