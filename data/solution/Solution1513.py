import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        current_length = 0
        
        for char in s:
            if char == '1':
                current_length += 1
                count = (count + current_length) % MOD
            else:
                current_length = 0
        
        return count

def numSub(s: str) -> int:
    return Solution().numSub(s)