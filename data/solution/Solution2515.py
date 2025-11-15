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
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_distance = float('inf')
        
        # Check if target exists in the list
        if target not in words:
            return -1
        
        # Iterate through the list to find the shortest distance
        for i in range(n):
            if words[i] == target:
                # Calculate the distance in both directions
                left_distance = (startIndex - i + n) % n
                right_distance = (i - startIndex + n) % n
                # Update the minimum distance
                min_distance = min(min_distance, left_distance, right_distance)
        
        return min_distance

def closestTarget(words: List[str], target: str, startIndex: int) -> int:
    return Solution().closestTarget(words, target, startIndex)