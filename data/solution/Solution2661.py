import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Create a dictionary to store the position of each number in the matrix
        position = {}
        m, n = len(mat), len(mat[0])
        
        for r in range(m):
            for c in range(n):
                position[mat[r][c]] = (r, c)
        
        # Initialize counters for rows and columns
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        
        # Iterate through the array and paint the cells
        for i, num in enumerate(arr):
            r, c = position[num]
            row_count[r] += 1
            col_count[c] += 1
            
            # Check if the current row or column is completely painted
            if row_count[r] == n or col_count[c] == m:
                return i

# Example usage:
# sol = Solution()
# print(sol.firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]))  # Output: 2
# print(sol.firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]))  # Output: 3

def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    return Solution().firstCompleteIndex(arr, mat)