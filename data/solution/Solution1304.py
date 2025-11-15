import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        # If n is even, we can simply add pairs of positive and negative numbers
        if n % 2 == 0:
            for i in range(1, n // 2 + 1):
                result.append(i)
                result.append(-i)
        else:
            # If n is odd, we add a zero in the middle
            for i in range(1, (n // 2) + 1):
                result.append(i)
                result.append(-i)
            result.append(0)
        
        return result

def sumZero(n: int) -> List[int]:
    return Solution().sumZero(n)