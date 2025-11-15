import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)
        
        # Step 1: Calculate prefix sums and prefix of prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD
        
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MOD
        
        # Step 2: Use monotonic stack to find next and previous smaller elements
        next_smaller = [n] * n
        prev_smaller_or_equal = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                next_smaller[stack.pop()] = i
            if stack:
                prev_smaller_or_equal[i] = stack[-1]
            stack.append(i)
        
        # Step 3: Calculate the total strength
        total_strength = 0
        
        for i in range(n):
            left = prev_smaller_or_equal[i]
            right = next_smaller[i]
            
            total_left = (i - left) * (prefix_prefix[right + 1] - prefix_prefix[i + 1]) % MOD
            total_right = (right - i) * (prefix_prefix[i + 1] - prefix_prefix[left + 1]) % MOD
            
            contribution = (strength[i] * (total_left - total_right)) % MOD
            total_strength = (total_strength + contribution) % MOD
        
        return total_strength

def totalStrength(strength: List[int]) -> int:
    return Solution().totalStrength(strength)