import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        
        for char in s:
            if char == 'L':
                balance += 1
            else:  # char == 'R'
                balance -= 1
            
            if balance == 0:
                count += 1
        
        return count

def balancedStringSplit(s: str) -> int:
    return Solution().balancedStringSplit(s)