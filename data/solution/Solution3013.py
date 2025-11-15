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
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        # The cost is always going to be at least nums[0]
        base_cost = nums[0]
        # We need to find the minimum sum of k-1 elements from the first dist+1 elements
        # because the second subarray can start at most at index dist
        
        # Using SortedList to maintain the smallest k-1 elements
        smallest_elements = SortedList(nums[1:dist+2])
        current_sum = sum(smallest_elements[:k-1])
        
        # The answer is initialized with the current sum of the smallest k-1 elements
        min_cost = base_cost + current_sum
        
        # Now, we slide the window of size dist+1 from index 2 to n-k+1
        for i in range(dist + 2, n):
            # Add the new element to the sorted list
            smallest_elements.add(nums[i])
            # Remove the element that is out of the current window
            smallest_elements.remove(nums[i - dist - 1])
            # Calculate the new sum of the smallest k-1 elements
            current_sum = sum(smallest_elements[:k-1])
            # Update the minimum cost
            min_cost = min(min_cost, base_cost + current_sum)
        
        return min_cost

def minimumCost(nums: List[int], k: int, dist: int) -> int:
    return Solution().minimumCost(nums, k, dist)