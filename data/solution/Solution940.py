import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        # dp[i] will store the number of distinct subsequences up to index i
        dp = [0] * (n + 1)
        dp[0] = 1  # There's one subsequence for an empty string: the empty subsequence itself
        
        # last_occurrence will store the last occurrence index of each character
        last_occurrence = {}
        
        for i, char in enumerate(s):
            dp[i + 1] = (2 * dp[i]) % MOD  # Double the count of subsequences up to the previous index
            
            if char in last_occurrence:
                # Subtract the subsequences that end with the same character before the last occurrence
                dp[i + 1] = (dp[i + 1] - dp[last_occurrence[char]] + MOD) % MOD
            
            # Update the last occurrence of the current character
            last_occurrence[char] = i
        
        # Subtract 1 to exclude the empty subsequence
        return (dp[n] - 1) % MOD

def distinctSubseqII(s: str) -> int:
    return Solution().distinctSubseqII(s)