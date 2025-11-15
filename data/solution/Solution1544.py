import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and char.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)

def makeGood(s: str) -> str:
    return Solution().makeGood(s)