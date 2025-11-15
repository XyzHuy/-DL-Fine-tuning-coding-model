import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Find the matching '(' and reverse the substring inside
                inner_bracket = []
                while stack[-1] != '(':
                    inner_bracket.append(stack.pop())
                # Pop the '('
                stack.pop()
                # Add the reversed substring back to the stack
                stack.extend(inner_bracket)
            else:
                # Add current character to the stack
                stack.append(char)
        
        # Join the stack to form the final string without parentheses
        return ''.join(stack)

def reverseParentheses(s: str) -> str:
    return Solution().reverseParentheses(s)