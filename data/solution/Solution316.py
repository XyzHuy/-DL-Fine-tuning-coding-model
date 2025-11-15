import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Dictionary to store the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        # Stack to build the result
        stack = []
        # Set to keep track of characters in the stack
        in_stack = set()
        
        for i, char in enumerate(s):
            # If the character is already in the stack, skip it
            if char in in_stack:
                continue
            
            # While the stack is not empty, and the current character is smaller than the last character in the stack
            # and the last character appears later in the string, pop it from the stack
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)
            
            # Add the current character to the stack and mark it as in the stack
            stack.append(char)
            in_stack.add(char)
        
        # Join the characters in the stack to form the result
        return ''.join(stack)

def removeDuplicateLetters(s: str) -> str:
    return Solution().removeDuplicateLetters(s)