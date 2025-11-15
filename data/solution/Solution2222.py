import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfWays(self, s: str) -> int:
        # Initialize counters for the number of 0s and 1s before and after each position
        n = len(s)
        zero_before = [0] * n
        one_before = [0] * n
        zero_after = [0] * n
        one_after = [0] * n
        
        # Fill zero_before and one_before arrays
        if s[0] == '0':
            zero_before[0] = 1
        else:
            one_before[0] = 1
        
        for i in range(1, n):
            zero_before[i] = zero_before[i - 1] + (1 if s[i] == '0' else 0)
            one_before[i] = one_before[i - 1] + (1 if s[i] == '1' else 0)
        
        # Fill zero_after and one_after arrays
        if s[n - 1] == '0':
            zero_after[n - 1] = 1
        else:
            one_after[n - 1] = 1
        
        for i in range(n - 2, -1, -1):
            zero_after[i] = zero_after[i + 1] + (1 if s[i] == '0' else 0)
            one_after[i] = one_after[i + 1] + (1 if s[i] == '1' else 0)
        
        # Calculate the number of valid ways to select 3 buildings
        count = 0
        for i in range(1, n - 1):
            if s[i] == '0':
                # We need patterns like 101
                count += one_before[i] * one_after[i]
            else:
                # We need patterns like 010
                count += zero_before[i] * zero_after[i]
        
        return count

def numberOfWays(s: str) -> int:
    return Solution().numberOfWays(s)