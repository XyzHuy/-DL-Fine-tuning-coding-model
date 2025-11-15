import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Create two reference strings of alternating patterns
        alt1 = '01' * (n // 2 + 1)
        alt2 = '10' * (n // 2 + 1)
        
        # Initial count of flips needed for the first window
        flips1 = sum(s[i] != alt1[i] for i in range(n))
        flips2 = sum(s[i] != alt2[i] for i in range(n))
        
        min_flips = min(flips1, flips2)
        
        # Use sliding window technique to check all possible rotations
        for i in range(n):
            # Remove the effect of the character that is sliding out of the window
            if s[i] != alt1[i]:
                flips1 -= 1
            if s[i] != alt2[i]:
                flips2 -= 1
            
            # Add the effect of the new character that is sliding into the window
            if s[i] != alt1[i + n % 2]:
                flips1 += 1
            if s[i] != alt2[i + n % 2]:
                flips2 += 1
            
            # Update the minimum flips needed
            min_flips = min(min_flips, flips1, flips2)
        
        return min_flips

def minFlips(s: str) -> int:
    return Solution().minFlips(s)