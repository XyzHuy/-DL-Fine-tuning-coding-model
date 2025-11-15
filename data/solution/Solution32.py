import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the last index from the stack for ')'
                if not stack:
                    stack.append(i)  # If stack is empty, push current index as base
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate the length of the current valid substring
        
        return max_length

def longestValidParentheses(s: str) -> int:
    return Solution().longestValidParentheses(s)