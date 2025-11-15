import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        
        # Count the frequency of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Calculate the total number of steps needed
        steps = 0
        for char in count_s:
            steps += max(0, count_s[char] - count_t[char])
        for char in count_t:
            steps += max(0, count_t[char] - count_s[char])
        
        return steps

def minSteps(s: str, t: str) -> int:
    return Solution().minSteps(s, t)