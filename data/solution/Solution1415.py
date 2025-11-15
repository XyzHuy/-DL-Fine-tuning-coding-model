import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Calculate the total number of happy strings of length n
        total_happy_strings = 3 * (1 << (n - 1))
        
        # If k is greater than the total number of happy strings, return an empty string
        if k > total_happy_strings:
            return ""
        
        # Initialize the result string
        result = []
        
        # Determine the starting character
        for i in range(2, -1, -1):
            if k > (1 << (n - 1)) * i:
                result.append(chr(ord('a') + i))
                k -= (1 << (n - 1)) * i
                break
        
        # Generate the rest of the string
        for i in range(n - 1):
            last_char = result[-1]
            if last_char == 'a':
                if k > (1 << (n - i - 2)):
                    result.append('c')
                    k -= (1 << (n - i - 2))
                else:
                    result.append('b')
            elif last_char == 'b':
                if k > (1 << (n - i - 2)):
                    result.append('c')
                    k -= (1 << (n - i - 2))
                else:
                    result.append('a')
            else:  # last_char == 'c'
                if k > (1 << (n - i - 2)):
                    result.append('b')
                    k -= (1 << (n - i - 2))
                else:
                    result.append('a')
        
        return ''.join(result)

def getHappyString(n: int, k: int) -> str:
    return Solution().getHappyString(n, k)