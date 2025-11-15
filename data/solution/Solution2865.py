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
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        
        # Initialize left and right arrays
        left = [0] * n
        right = [0] * n
        
        # Stack for left
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = left[stack[-1]] + heights[i] * (i - stack[-1])
            else:
                left[i] = heights[i] * (i + 1)
            stack.append(i)
        
        # Stack for right
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = right[stack[-1]] + heights[i] * (stack[-1] - i)
            else:
                right[i] = heights[i] * (n - i)
            stack.append(i)
        
        # Calculate the maximum sum of heights for mountain shape
        max_sum = 0
        for i in range(n):
            max_sum = max(max_sum, left[i] + right[i] - heights[i])
        
        return max_sum

def maximumSumOfHeights(heights: List[int]) -> int:
    return Solution().maximumSumOfHeights(heights)