import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = [float('inf')] * n
        result = [0] * n
        
        for i, height in enumerate(obstacles):
            # Find the position to replace in dp array
            pos = bisect.bisect_right(dp, height)
            dp[pos] = height
            result[i] = pos + 1
        
        return result

def longestObstacleCourseAtEachPosition(obstacles: List[int]) -> List[int]:
    return Solution().longestObstacleCourseAtEachPosition(obstacles)