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
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Initialize the array with zeros
        arr = [0] * length
        
        # Apply the difference array technique
        for startIdx, endIdx, inc in updates:
            arr[startIdx] += inc
            if endIdx + 1 < length:
                arr[endIdx + 1] -= inc
        
        # Convert the difference array to the final array
        for i in range(1, length):
            arr[i] += arr[i - 1]
        
        return arr

def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
    return Solution().getModifiedArray(length, updates)