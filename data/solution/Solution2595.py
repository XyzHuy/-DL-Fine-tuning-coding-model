import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even_count = 0
        odd_count = 0
        index = 0
        
        while n > 0:
            if n & 1:  # Check if the least significant bit is 1
                if index % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            n >>= 1  # Right shift n to check the next bit
            index += 1
        
        return [even_count, odd_count]

def evenOddBit(n: int) -> List[int]:
    return Solution().evenOddBit(n)