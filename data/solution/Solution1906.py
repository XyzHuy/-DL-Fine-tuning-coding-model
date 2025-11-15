import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Create a dictionary to store the indices of each number in nums
        num_indices = defaultdict(list)
        for i, num in enumerate(nums):
            num_indices[num].append(i)
        
        # Function to find the minimum absolute difference in the subarray nums[left:right+1]
        def min_diff_in_range(left, right):
            # Get all unique numbers in the range
            unique_nums = set()
            for num, indices in num_indices.items():
                # Check if the number appears in the range [left, right]
                if any(left <= index <= right for index in indices):
                    unique_nums.add(num)
            
            # If there's only one unique number, return -1
            if len(unique_nums) < 2:
                return -1
            
            # Sort the unique numbers and find the minimum difference
            sorted_unique_nums = sorted(unique_nums)
            min_diff = float('inf')
            for i in range(len(sorted_unique_nums) - 1):
                min_diff = min(min_diff, sorted_unique_nums[i + 1] - sorted_unique_nums[i])
            
            return min_diff
        
        # Process each query
        result = []
        for left, right in queries:
            result.append(min_diff_in_range(left, right))
        
        return result

def minDifference(nums: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().minDifference(nums, queries)