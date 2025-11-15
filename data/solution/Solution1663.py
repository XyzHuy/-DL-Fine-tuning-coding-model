import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # Start by filling the string with 'a'
        result = ['a'] * n
        # The remaining value to be distributed
        k -= n
        
        # Fill the string from the end to make it lexicographically smallest
        while k > 0:
            # Calculate the value to be added to make the current character as large as possible
            add = min(25, k)  # We can add at most 25 to change 'a' to 'z'
            result[n - 1] = chr(ord(result[n - 1]) + add)
            k -= add
            n -= 1
        
        return ''.join(result)

def getSmallestString(n: int, k: int) -> str:
    return Solution().getSmallestString(n, k)