import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def is_balanced(sub):
            from collections import Counter
            count = Counter(sub)
            freqs = set(count.values())
            return len(freqs) == 1
        
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(i):
                if is_balanced(s[j:i]):
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n]

def minimumSubstringsInPartition(s: str) -> int:
    return Solution().minimumSubstringsInPartition(s)