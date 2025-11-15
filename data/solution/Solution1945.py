import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string into an integer
        # by replacing each letter with its position in the alphabet
        number_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2 and 3: Transform the integer by summing its digits k times
        for _ in range(k):
            number_str = str(sum(int(digit) for digit in number_str))
        
        # Convert the final result back to an integer and return
        return int(number_str)

def getLucky(s: str, k: int) -> int:
    return Solution().getLucky(s, k)