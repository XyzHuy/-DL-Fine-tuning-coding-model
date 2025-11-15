import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        prev = [-1] * n
        next = [n] * n
        
        # Dictionary to store the last seen index of each character
        last_seen = {}
        
        # Fill the prev array
        for i in range(n):
            if s[i] in last_seen:
                prev[i] = last_seen[s[i]]
            last_seen[s[i]] = i
        
        # Reset the last_seen dictionary
        last_seen = {}
        
        # Fill the next array
        for i in range(n-1, -1, -1):
            if s[i] in last_seen:
                next[i] = last_seen[s[i]]
            last_seen[s[i]] = i
        
        # Calculate the sum of unique characters for all substrings
        result = 0
        for i in range(n):
            result += (i - prev[i]) * (next[i] - i)
        
        return result % (10**9 + 7)

def uniqueLetterString(s: str) -> int:
    return Solution().uniqueLetterString(s)