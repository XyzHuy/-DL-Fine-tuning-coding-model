import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Initialize prefix sums array with 0 to handle prefix starting from index 0
        prefix_sums = [0]
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            # We need to find the range of prefix sums that would result in a valid range sum with current_sum
            # Such that lower <= current_sum - prefix_sum <= upper
            # This can be rewritten as current_sum - upper <= prefix_sum <= current_sum - lower
            lower_bound = current_sum - upper
            upper_bound = current_sum - lower
            
            # Use binary search to find the number of valid prefix sums
            count += bisect.bisect_right(prefix_sums, upper_bound) - bisect.bisect_left(prefix_sums, lower_bound)
            
            # Insert the current prefix sum into the sorted list of prefix sums
            bisect.insort(prefix_sums, current_sum)
        
        return count

def countRangeSum(nums: List[int], lower: int, upper: int) -> int:
    return Solution().countRangeSum(nums, lower, upper)