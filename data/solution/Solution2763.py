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

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        def imbalance_of_subarray(subarr):
            sarr = sorted(subarr)
            imbalance = 0
            for i in range(len(sarr) - 1):
                if sarr[i + 1] - sarr[i] > 1:
                    imbalance += 1
            return imbalance
        
        total_imbalance = 0
        n = len(nums)
        
        for start in range(n):
            for end in range(start, n):
                subarr = nums[start:end + 1]
                total_imbalance += imbalance_of_subarray(subarr)
        
        return total_imbalance

def sumImbalanceNumbers(nums: List[int]) -> int:
    return Solution().sumImbalanceNumbers(nums)