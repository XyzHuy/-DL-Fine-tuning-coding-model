import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        from collections import Counter
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        # Stack to store the result characters
        stack = []
        # Set to keep track of characters in the stack
        in_stack = set()
        
        for char in s:
            # Decrease the count of the current character
            char_count[char] -= 1
            
            # If the character is not already in the stack
            if char not in in_stack:
                # While the stack is not empty, the last character in the stack is greater than the current character,
                # and the last character will appear later in the string, remove it from the stack
                while stack and stack[-1] > char and char_count[stack[-1]] > 0:
                    removed_char = stack.pop()
                    in_stack.remove(removed_char)
                
                # Add the current character to the stack and mark it as in the stack
                stack.append(char)
                in_stack.add(char)
        
        # Join the characters in the stack to form the result string
        return ''.join(stack)

def smallestSubsequence(s: str) -> str:
    return Solution().smallestSubsequence(s)