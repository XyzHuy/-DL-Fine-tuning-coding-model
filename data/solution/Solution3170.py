import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def clearStars(self, s: str) -> str:
        # Stack to keep track of characters
        stack = []
        
        for char in s:
            if char == '*':
                if stack:
                    # Remove the smallest character to the left of '*'
                    # We do this by popping elements until we find the smallest
                    min_char = stack[-1]
                    min_index = len(stack) - 1
                    for i in range(len(stack) - 2, -1, -1):
                        if stack[i] < min_char:
                            min_char = stack[i]
                            min_index = i
                    # Remove the smallest character found
                    stack.pop(min_index)
            else:
                stack.append(char)
        
        return ''.join(stack)

def clearStars(s: str) -> str:
    return Solution().clearStars(s)