import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            dp[i] = points
            if i + brainpower + 1 < n:
                dp[i] += dp[i + brainpower + 1]
            if i + 1 < n:
                dp[i] = max(dp[i], dp[i + 1])
        
        return dp[0]

def mostPoints(questions: List[List[int]]) -> int:
    return Solution().mostPoints(questions)