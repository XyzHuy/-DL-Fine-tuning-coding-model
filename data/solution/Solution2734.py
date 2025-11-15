import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestString(self, s: str) -> str:
        # Find the first non-'a' character
        start = 0
        while start < len(s) and s[start] == 'a':
            start += 1
        
        # If the entire string is 'a's, change the last 'a' to 'z'
        if start == len(s):
            return s[:-1] + 'z'
        
        # Find the end of the substring to be decremented
        end = start
        while end < len(s) and s[end] != 'a':
            end += 1
        
        # Decrement the characters in the substring from start to end-1
        result = s[:start] + ''.join(chr(ord(c) - 1) for c in s[start:end]) + s[end:]
        
        return result

def smallestString(s: str) -> str:
    return Solution().smallestString(s)