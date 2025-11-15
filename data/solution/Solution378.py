import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def countLessEqual(mid):
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    row -= 1
                else:
                    count += row + 1
                    col += 1
            return count
        
        low, high = matrix[0][0], matrix[n-1][n-1]
        
        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    return Solution().kthSmallest(matrix, k)