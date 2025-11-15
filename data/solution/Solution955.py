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
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs or not strs[0]:
            return 0
        
        num_rows, num_cols = len(strs), len(strs[0])
        deletions = 0
        sorted_until = [False] * num_rows
        
        for col in range(num_cols):
            # Check if the current column is sorted
            is_sorted = True
            for row in range(1, num_rows):
                if not sorted_until[row] and strs[row][col] < strs[row - 1][col]:
                    is_sorted = False
                    break
            
            if not is_sorted:
                deletions += 1
            else:
                # Mark rows as sorted until this column
                for row in range(1, num_rows):
                    if not sorted_until[row] and strs[row][col] > strs[row - 1][col]:
                        sorted_until[row] = True
        
        return deletions

def minDeletionSize(strs: List[str]) -> int:
    return Solution().minDeletionSize(strs)