import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Initialize a counter to keep track of the number of valid substrings
        count = 0
        # Dictionary to store the last seen index of characters 'a', 'b', and 'c'
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        # Variable to store the length of the string
        n = len(s)
        
        # Iterate over the string
        for i in range(n):
            # Update the last seen index of the current character
            last_seen[s[i]] = i
            # The number of valid substrings ending at index i is the index of the smallest last seen index of 'a', 'b', and 'c' plus 1
            count += min(last_seen.values()) + 1
        
        return count

def numberOfSubstrings(s: str) -> int:
    return Solution().numberOfSubstrings(s)