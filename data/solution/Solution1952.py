import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isThree(self, n: int) -> bool:
        # A number n has exactly three positive divisors if and only if
        # it is the square of a prime number. This is because the divisors
        # would be 1, p, and p^2 where p is a prime number.
        
        if n < 4:
            return False  # The smallest number with exactly three divisors is 4 (2^2)
        
        count = 0
        root = int(n**0.5)
        
        # Check if root is an integer and if it is a prime number
        if root * root != n:
            return False
        
        # Check if root is a prime number
        for i in range(2, int(root**0.5) + 1):
            if root % i == 0:
                return False
        
        return True

def isThree(n: int) -> bool:
    return Solution().isThree(n)