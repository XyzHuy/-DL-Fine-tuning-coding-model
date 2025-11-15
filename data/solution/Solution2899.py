import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        consecutive_neg_ones = 0
        
        for num in nums:
            if num != -1:
                # Prepend the positive integer to the front of seen
                seen.insert(0, num)
                # Reset consecutive_neg_ones counter
                consecutive_neg_ones = 0
            else:
                # Increment the consecutive_neg_ones counter
                consecutive_neg_ones += 1
                # Check if k is less than or equal to the length of seen
                if consecutive_neg_ones <= len(seen):
                    # Append the k-th element of seen to ans
                    ans.append(seen[consecutive_neg_ones - 1])
                else:
                    # Append -1 to ans
                    ans.append(-1)
        
        return ans

def lastVisitedIntegers(nums: List[int]) -> List[int]:
    return Solution().lastVisitedIntegers(nums)