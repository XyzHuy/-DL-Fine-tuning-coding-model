import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        diff_array = [nums1[i] - nums2[i] for i in range(n)]
        
        sorted_list = SortedList()
        count = 0
        
        for num in diff_array:
            # Count elements in sorted_list that are <= num + diff
            count += sorted_list.bisect_right(num + diff)
            # Add current num to the sorted_list
            sorted_list.add(num)
        
        return count

# Example usage:
# sol = Solution()
# print(sol.numberOfPairs([3, 2, 5], [2, 2, 1], 1))  # Output: 3
# print(sol.numberOfPairs([3, -1], [-2, 2], -1))  # Output: 0

def numberOfPairs(nums1: List[int], nums2: List[int], diff: int) -> int:
    return Solution().numberOfPairs(nums1, nums2, diff)