import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        
        # Calculate the size of the decoded string
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
        
        # Traverse the string in reverse to find the k-th character
        for char in reversed(s):
            k %= size
            
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                size //= int(char)
            else:
                size -= 1

def decodeAtIndex(s: str, k: int) -> str:
    return Solution().decodeAtIndex(s, k)