import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for char in s:
            if stack and (char == 'B' and stack[-1] == 'A' or char == 'D' and stack[-1] == 'C'):
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack)

def minLength(s: str) -> int:
    return Solution().minLength(s)