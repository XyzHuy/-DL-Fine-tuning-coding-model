import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isNumber(self, s: str) -> bool:
        def scan_integer(s, idx):
            if idx < len(s) and (s[idx] == '+' or s[idx] == '-'):
                idx += 1
            return scan_unsigned_integer(s, idx)
        
        def scan_unsigned_integer(s, idx):
            before = idx
            while idx < len(s) and '0' <= s[idx] <= '9':
                idx += 1
            return idx > before, idx
        
        if not s:
            return False
        
        idx = 0
        is_numeric, idx = scan_integer(s, idx)
        
        if idx < len(s) and s[idx] == '.':
            idx += 1
            has_fraction, idx = scan_unsigned_integer(s, idx)
            is_numeric = is_numeric or has_fraction
        
        if idx < len(s) and (s[idx] == 'e' or s[idx] == 'E'):
            idx += 1
            has_exponent, idx = scan_integer(s, idx)
            is_numeric = is_numeric and has_exponent
        
        return is_numeric and idx == len(s)

def isNumber(s: str) -> bool:
    return Solution().isNumber(s)