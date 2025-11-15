import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary_set = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1  # Assume the current character is an extra character
            for j in range(i):
                if s[j:i] in dictionary_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]

def minExtraChar(s: str, dictionary: List[str]) -> int:
    return Solution().minExtraChar(s, dictionary)