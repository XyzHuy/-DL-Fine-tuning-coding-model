import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def parseTernary(self, expression: str) -> str:
        def evaluate(index):
            # Base case: if the current character is a digit or 'T'/'F', return it
            if index == len(expression) - 1 or expression[index + 1] == ':':
                return expression[index], index + 2
            
            # Recursive case: process the ternary expression
            if expression[index] == 'T':
                # If the condition is true, evaluate the true branch
                result, new_index = evaluate(index + 2)
            else:
                # If the condition is false, skip the true branch and evaluate the false branch
                # Find the matching ':' for the current '?'
                balance = 1
                new_index = index + 2
                while balance > 0:
                    if expression[new_index] == '?':
                        balance += 1
                    elif expression[new_index] == ':':
                        balance -= 1
                    new_index += 1
                result, new_index = evaluate(new_index)
            
            return result, new_index
        
        result, _ = evaluate(0)
        return result

def parseTernary(expression: str) -> str:
    return Solution().parseTernary(expression)