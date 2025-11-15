import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If k is divisible by 2 or 5, there is no such n
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        # Initialize variables
        remainder = 0
        length = 0
        
        # Loop until we find a remainder of 0
        while True:
            # Append a digit 1 to the current remainder
            remainder = (remainder * 10 + 1) % k
            length += 1
            
            # If the remainder is 0, we found the answer
            if remainder == 0:
                return length

def smallestRepunitDivByK(k: int) -> int:
    return Solution().smallestRepunitDivByK(k)