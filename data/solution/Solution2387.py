import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Find the minimum and maximum elements in the matrix
        min_element = float('inf')
        max_element = float('-inf')
        for row in grid:
            min_element = min(min_element, row[0])
            max_element = max(max_element, row[-1])
        
        # Function to count elements less than or equal to x
        def countLessEqual(x: int) -> int:
            count = 0
            for row in grid:
                # Binary search to find the count of elements <= x in each row
                count += self.countInRow(row, x)
            return count
        
        # Binary search on the range between min_element and max_element
        left, right = min_element, max_element
        while left < right:
            mid = left + (right - left) // 2
            if countLessEqual(mid) >= (total_elements + 1) // 2:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    # Helper function to count elements <= x in a sorted row using binary search
    def countInRow(self, row: List[int], x: int) -> int:
        low, high = 0, len(row)
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] <= x:
                low = mid + 1
            else:
                high = mid
        return low

def matrixMedian(grid: List[List[int]]) -> int:
    return Solution().matrixMedian(grid)