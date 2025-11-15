import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def get_kth_smallest(trim_length, k):
            # Create a list of tuples (trimmed number, original index)
            trimmed_nums = [(num[-trim_length:], idx) for idx, num in enumerate(nums)]
            # Sort the list by the trimmed number, and by the original index if tied
            trimmed_nums.sort()
            # Return the original index of the k-th smallest trimmed number
            return trimmed_nums[k-1][1]
        
        # Process each query
        result = []
        for k, trim_length in queries:
            result.append(get_kth_smallest(trim_length, k))
        
        return result

def smallestTrimmedNumbers(nums: List[str], queries: List[List[int]]) -> List[int]:
    return Solution().smallestTrimmedNumbers(nums, queries)