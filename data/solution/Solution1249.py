import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Stack to keep track of indices of '('
        stack = []
        # List to keep track of characters to remove
        remove = set()
        
        # First pass to find unmatched ')'
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        
        # Add remaining unmatched '(' to the remove set
        remove.update(stack)
        
        # Build the result string excluding the characters in the remove set
        result = []
        for i, char in enumerate(s):
            if i not in remove:
                result.append(char)
        
        return ''.join(result)

def minRemoveToMakeValid(s: str) -> str:
    return Solution().minRemoveToMakeValid(s)