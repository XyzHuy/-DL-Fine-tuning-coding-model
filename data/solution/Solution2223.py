import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sumScores(self, s: str) -> int:
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z
        
        # Calculate the Z-function for the string
        z_values = z_function(s)
        
        # The score for s_n (the full string) is n
        total_score = len(s)
        
        # Add the scores for all other prefixes
        total_score += sum(z_values)
        
        return total_score

def sumScores(s: str) -> int:
    return Solution().sumScores(s)