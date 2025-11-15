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
from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # Initialize arrays to store whether we can reach the end starting from each index
        odd_jump = [False] * n
        even_jump = [False] * n
        
        # The last index is always a good starting point
        odd_jump[n - 1] = True
        even_jump[n - 1] = True
        
        # Sorted dictionary to keep track of the indices in sorted order of values
        sorted_dict = SortedDict()
        sorted_dict[arr[n - 1]] = n - 1
        
        # Iterate from the second last element to the first
        for i in range(n - 2, -1, -1):
            # Find the smallest element greater than or equal to arr[i]
            key = sorted_dict.bisect_left(arr[i])
            if key < len(sorted_dict):
                next_index = sorted_dict.values()[key]
                odd_jump[i] = even_jump[next_index]
            
            # Find the largest element less than or equal to arr[i]
            key = sorted_dict.bisect_right(arr[i]) - 1
            if key >= 0:
                next_index = sorted_dict.values()[key]
                even_jump[i] = odd_jump[next_index]
            
            # Insert the current element into the sorted dictionary
            sorted_dict[arr[i]] = i
        
        # Count the number of good starting points
        return sum(odd_jump)

def oddEvenJumps(arr: List[int]) -> int:
    return Solution().oddEvenJumps(arr)