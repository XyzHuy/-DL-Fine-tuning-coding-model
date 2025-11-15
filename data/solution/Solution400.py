import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findNthDigit(self, n: int) -> int:
        # Determine the number of digits in the number that contains the nth digit
        length = 1
        count = 9
        start = 1
        
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Find the actual number that contains the nth digit
        start += (n - 1) // length
        
        # Find the nth digit in the number
        return int(str(start)[(n - 1) % length])

def findNthDigit(n: int) -> int:
    return Solution().findNthDigit(n)