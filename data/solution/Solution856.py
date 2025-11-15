import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + (2 * score if score else 1)
        
        return score

def scoreOfParentheses(s: str) -> int:
    return Solution().scoreOfParentheses(s)