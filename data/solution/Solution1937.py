import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]
        
        for r in range(1, m):
            left_max = [0] * n
            right_max = [0] * n
            
            # Fill left_max
            left_max[0] = dp[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j - 1] - 1, dp[j])
            
            # Fill right_max
            right_max[-1] = dp[-1]
            for j in range(n - 2, -1, -1):
                right_max[j] = max(right_max[j + 1] - 1, dp[j])
            
            # Update dp for the current row
            for j in range(n):
                dp[j] = points[r][j] + max(left_max[j], right_max[j])
        
        return max(dp)

def maxPoints(points: List[List[int]]) -> int:
    return Solution().maxPoints(points)