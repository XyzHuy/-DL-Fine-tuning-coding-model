import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        # Iterate through possible split points
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            max_score = max(max_score, score)
        return max_score

def maxScore(s: str) -> int:
    return Solution().maxScore(s)