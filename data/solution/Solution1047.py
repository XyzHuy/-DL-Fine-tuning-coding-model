import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

def removeDuplicates(s: str) -> str:
    return Solution().removeDuplicates(s)