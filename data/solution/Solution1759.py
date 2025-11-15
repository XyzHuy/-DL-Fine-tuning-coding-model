import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if n == 0:
            return 0
        
        count = 0
        current_char = s[0]
        current_length = 1
        
        for i in range(1, n):
            if s[i] == current_char:
                current_length += 1
            else:
                # Calculate the number of homogenous substrings for the current segment
                count += (current_length * (current_length + 1)) // 2
                count %= MOD
                
                # Reset for the new character
                current_char = s[i]
                current_length = 1
        
        # Add the last segment
        count += (current_length * (current_length + 1)) // 2
        count %= MOD
        
        return count

def countHomogenous(s: str) -> int:
    return Solution().countHomogenous(s)