import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        # Compute prefix sums
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        answer = []
        
        for q in queries:
            # Find the index where q would be inserted to keep nums sorted
            idx = bisect.bisect_left(nums, q)
            
            # Calculate the number of operations needed
            # Operations to make elements before idx equal to q
            left_operations = q * idx - prefix_sum[idx]
            # Operations to make elements at or after idx equal to q
            right_operations = (prefix_sum[n] - prefix_sum[idx]) - q * (n - idx)
            
            # Total operations for this query
            answer.append(left_operations + right_operations)
        
        return answer

def minOperations(nums: List[int], queries: List[int]) -> List[int]:
    return Solution().minOperations(nums, queries)