import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # Create a prefix sum matrix
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        
        # Function to check if a square of side length `length` with top-left corner at (i, j) has sum <= threshold
        def is_valid_square(i, j, length):
            if i + length > m or j + length > n:
                return False
            total_sum = prefix_sum[i + length][j + length] - prefix_sum[i + length][j] - prefix_sum[i][j + length] + prefix_sum[i][j]
            return total_sum <= threshold
        
        # Binary search for the maximum side length
        left, right = 0, min(m, n) + 1
        while left < right:
            mid = (left + right) // 2
            found = False
            for i in range(m):
                for j in range(n):
                    if is_valid_square(i, j, mid):
                        found = True
                        break
                if found:
                    break
            if found:
                left = mid + 1
            else:
                right = mid
        
        # Since right is the first invalid side length, the maximum valid side length is right - 1
        return right - 1

def maxSideLength(mat: List[List[int]], threshold: int) -> int:
    return Solution().maxSideLength(mat, threshold)