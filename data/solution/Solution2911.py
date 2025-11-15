import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        def min_changes_to_semi_palindrome(sub):
            m = len(sub)
            min_changes = float('inf')
            for d in range(1, m):
                if m % d != 0:
                    continue
                changes = 0
                for i in range(d):
                    group = [sub[j] for j in range(i, m, d)]
                    half_len = len(group) // 2
                    for l in range(half_len):
                        if group[l] != group[-(l + 1)]:
                            changes += 1
                min_changes = min(min_changes, changes)
            return min_changes
        
        # Initialize DP table
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for start in range(i):
                    sub = s[start:i]
                    changes = min_changes_to_semi_palindrome(sub)
                    dp[i][j] = min(dp[i][j], dp[start][j - 1] + changes)
        
        return dp[n][k]

def minimumChanges(s: str, k: int) -> int:
    return Solution().minimumChanges(s, k)