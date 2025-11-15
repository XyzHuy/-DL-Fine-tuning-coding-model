import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            if balance > 1:
                result.append(char)
            if char == ')':
                balance -= 1
        
        return ''.join(result)

def removeOuterParentheses(s: str) -> str:
    return Solution().removeOuterParentheses(s)