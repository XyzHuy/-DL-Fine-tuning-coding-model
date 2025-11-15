import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def largestInteger(self, num: int) -> int:
        # Convert the number to a list of digits
        digits = list(map(int, str(num)))
        
        # Separate the digits into odd and even lists
        odds = [d for d in digits if d % 2 != 0]
        evens = [d for d in digits if d % 2 == 0]
        
        # Sort the odd and even lists in descending order
        odds.sort(reverse=True)
        evens.sort(reverse=True)
        
        # Create an iterator for each sorted list
        odd_iter = iter(odds)
        even_iter = iter(evens)
        
        # Reconstruct the number by choosing the largest available digit
        # with the same parity as the original digit
        result = []
        for d in digits:
            if d % 2 != 0:
                result.append(next(odd_iter))
            else:
                result.append(next(even_iter))
        
        # Convert the result list back to an integer
        return int(''.join(map(str, result)))

def largestInteger(num: int) -> int:
    return Solution().largestInteger(num)