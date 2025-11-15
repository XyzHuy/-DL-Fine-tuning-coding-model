import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold the mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []

        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all opening brackets were matched correctly
        return not stack

def isValid(s: str) -> bool:
    return Solution().isValid(s)