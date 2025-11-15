import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_length = 0
        i = 0
        n = len(s)
        
        while i < n:
            count_zeros = 0
            count_ones = 0
            
            # Count consecutive zeros
            while i < n and s[i] == '0':
                count_zeros += 1
                i += 1
            
            # Count consecutive ones
            while i < n and s[i] == '1':
                count_ones += 1
                i += 1
            
            # Calculate the length of the balanced substring
            balanced_length = 2 * min(count_zeros, count_ones)
            max_length = max(max_length, balanced_length)
        
        return max_length

def findTheLongestBalancedSubstring(s: str) -> int:
    return Solution().findTheLongestBalancedSubstring(s)