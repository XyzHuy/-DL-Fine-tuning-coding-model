import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestNumber(self, n: int) -> str:
        if n < 10:
            return str(n)
        
        digits = []
        
        # Try to factorize n using digits from 9 to 2
        for d in range(9, 1, -1):
            while n % d == 0:
                digits.append(d)
                n //= d
        
        # If n is not reduced to 1, it means it has a prime factor greater than 9
        if n != 1:
            return "-1"
        
        # Sort digits to form the smallest number
        digits.sort()
        
        # Join digits to form the result
        return ''.join(map(str, digits))

def smallestNumber(n: int) -> str:
    return Solution().smallestNumber(n)