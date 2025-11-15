import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        current_power = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_power += 1
            else:
                max_power = max(max_power, current_power)
                current_power = 1
        
        # Final check to ensure the last sequence is considered
        max_power = max(max_power, current_power)
        
        return max_power

def maxPower(s: str) -> int:
    return Solution().maxPower(s)