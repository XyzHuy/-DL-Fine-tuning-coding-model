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
import heapq

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        first_greater_stack = []
        second_greater_heap = []

        for i, num in enumerate(nums):
            # Process elements in the heap that have found their second greater element
            while second_greater_heap and second_greater_heap[0][0] < num:
                _, index = heapq.heappop(second_greater_heap)
                result[index] = num
            
            # Process elements in the stack that have found their first greater element
            while first_greater_stack and nums[first_greater_stack[-1]] < num:
                index = first_greater_stack.pop()
                heapq.heappush(second_greater_heap, (nums[index], index))
            
            # Push the current index onto the stack
            first_greater_stack.append(i)
        
        return result

# Example usage:
# sol = Solution()
# print(sol.secondGreaterElement([2, 4, 0, 9, 6]))  # Output: [9, 6, 6, -1, -1]
# print(sol.secondGreaterElement([3, 3]))          # Output: [-1, -1]

def secondGreaterElement(nums: List[int]) -> List[int]:
    return Solution().secondGreaterElement(nums)