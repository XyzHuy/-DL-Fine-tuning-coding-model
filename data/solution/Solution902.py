import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # Convert n to a string to easily access each digit
        n_str = str(n)
        n_len = len(n_str)
        digits_len = len(digits)
        
        # Count numbers with fewer digits than n
        count = 0
        for i in range(1, n_len):
            count += digits_len ** i
        
        # Count numbers with the same number of digits as n
        for i in range(n_len):
            found_match = False
            for d in digits:
                if d < n_str[i]:
                    count += digits_len ** (n_len - i - 1)
                elif d == n_str[i]:
                    found_match = True
                    break
            if not found_match:
                return count
        
        # If we matched all digits exactly, add 1 for the number n itself
        return count + 1

def atMostNGivenDigitSet(digits: List[str], n: int) -> int:
    return Solution().atMostNGivenDigitSet(digits, n)