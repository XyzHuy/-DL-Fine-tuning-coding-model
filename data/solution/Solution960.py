import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        
        # dp[i] will store the length of the longest increasing subsequence ending at index i
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The maximum length of increasing subsequence gives us the columns to keep
        # The minimum number of deletions is the total number of columns minus this length
        return n - max(dp)

def minDeletionSize(strs: List[str]) -> int:
    return Solution().minDeletionSize(strs)