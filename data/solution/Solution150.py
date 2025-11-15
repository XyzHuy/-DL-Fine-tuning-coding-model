import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                # Pop the two top elements from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation and push the result back onto the stack
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Use int() for truncating division towards zero
                    stack.append(int(a / b))
        
        # The final result is the only element left in the stack
        return stack[0]

def evalRPN(tokens: List[str]) -> int:
    return Solution().evalRPN(tokens)