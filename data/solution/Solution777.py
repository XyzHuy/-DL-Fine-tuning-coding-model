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
    def canTransform(self, start: str, result: str) -> bool:
        # Remove 'X' from both strings to get the order of 'L' and 'R'
        filtered_start = [ch for ch in start if ch != 'X']
        filtered_result = [ch for ch in result if ch != 'X']
        
        # If the order of 'L' and 'R' is different, return False
        if filtered_start != filtered_result:
            return False
        
        # Check the positions of 'L' and 'R'
        start_L_positions = [i for i, ch in enumerate(start) if ch == 'L']
        result_L_positions = [i for i, ch in enumerate(result) if ch == 'L']
        
        start_R_positions = [i for i, ch in enumerate(start) if ch == 'R']
        result_R_positions = [i for i, ch in enumerate(result) if ch == 'R']
        
        # 'L' can only move to the left, so each 'L' in start must be at least as far left as in result
        for s, r in zip(start_L_positions, result_L_positions):
            if s < r:
                return False
        
        # 'R' can only move to the right, so each 'R' in start must be at least as far right as in result
        for s, r in zip(start_R_positions, result_R_positions):
            if s > r:
                return False
        
        return True

def canTransform(start: str, result: str) -> bool:
    return Solution().canTransform(start, result)