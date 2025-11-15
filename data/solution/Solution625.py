import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10:
            return num
        
        factors = []
        for i in range(9, 1, -1):
            while num % i == 0:
                factors.append(i)
                num //= i
        
        if num != 1:
            return 0
        
        factors.sort()
        result = int(''.join(map(str, factors)))
        
        if result > 2**31 - 1:
            return 0
        
        return result

def smallestFactorization(num: int) -> int:
    return Solution().smallestFactorization(num)