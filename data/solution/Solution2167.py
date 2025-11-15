import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)
        # Initialize dp arrays
        dp_left = [0] * (n + 1)
        dp_right = [0] * (n + 1)
        
        # Fill dp_left array
        for i in range(n):
            if s[i] == '0':
                dp_left[i + 1] = dp_left[i]
            else:
                dp_left[i + 1] = min(dp_left[i] + 2, i + 1)
        
        # Fill dp_right array
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp_right[i] = dp_right[i + 1]
            else:
                dp_right[i] = min(dp_right[i + 1] + 2, n - i)
        
        # Calculate the minimum time
        min_time = float('inf')
        for i in range(n + 1):
            min_time = min(min_time, dp_left[i] + dp_right[i])
        
        return min_time

def minimumTime(s: str) -> int:
    return Solution().minimumTime(s)