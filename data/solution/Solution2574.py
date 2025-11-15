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
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]
        
        answer = [abs(leftSum[i] - rightSum[i]) for i in range(n)]
        
        return answer

def leftRightDifference(nums: List[int]) -> List[int]:
    return Solution().leftRightDifference(nums)