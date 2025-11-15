import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))
        
        result = []
        
        def backtrack(current_number, length):
            if length == n:
                result.append(current_number)
                return
            
            last_digit = current_number % 10
            
            # Add the next digit if it's valid
            if last_digit + k < 10:
                backtrack(current_number * 10 + (last_digit + k), length + 1)
            
            # Avoid adding the same digit twice when k == 0
            if k != 0 and last_digit - k >= 0:
                backtrack(current_number * 10 + (last_digit - k), length + 1)
        
        # Start with digits 1 through 9 (no leading zeros)
        for i in range(1, 10):
            backtrack(i, 1)
        
        return result

def numsSameConsecDiff(n: int, k: int) -> List[int]:
    return Solution().numsSameConsecDiff(n, k)