import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        def is_palindrome(s):
            return s == s[::-1]
        
        n = len(a)
        
        # Check if there's a valid split for a + b or b + a
        for i in range(n + 1):
            # Split a into aprefix and asuffix, and b into bprefix and bsuffix
            aprefix, asuffix = a[:i], a[i:]
            bprefix, bsuffix = b[:i], b[i:]
            
            # Check if aprefix + bsuffix or bprefix + asuffix is a palindrome
            if is_palindrome(aprefix + bsuffix) or is_palindrome(bprefix + asuffix):
                return True
        
        return False

def checkPalindromeFormation(a: str, b: str) -> bool:
    return Solution().checkPalindromeFormation(a, b)