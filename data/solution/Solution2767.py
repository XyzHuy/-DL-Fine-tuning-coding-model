import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        # Precompute the binary representations of powers of 5 that fit within the given constraints
        powers_of_5 = set()
        power = 1
        while power <= int('1' * 15, 2):  # The maximum possible value for a binary string of length 15
            powers_of_5.add(bin(power)[2:])
            power *= 5
        
        # Initialize a DP array where dp[i] represents the minimum number of beautiful substrings for the first i characters
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 substrings for an empty string
        
        # Fill the DP array
        for i in range(1, n + 1):
            for j in range(i):
                # Check if the substring s[j:i] is a beautiful substring
                if s[j] != '0' and s[j:i] in powers_of_5:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        # If dp[n] is still infinity, it means we couldn't partition the string into beautiful substrings
        return dp[n] if dp[n] != float('inf') else -1

def minimumBeautifulSubstrings(s: str) -> int:
    return Solution().minimumBeautifulSubstrings(s)