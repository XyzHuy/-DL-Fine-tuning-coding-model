import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimizeResult(self, expression: str) -> str:
        # Split the expression into left and right parts
        left, right = expression.split('+')
        
        # Initialize variables to keep track of the minimum value and the best positions for parentheses
        min_value = float('inf')
        best_left_pos = best_right_pos = -1
        
        # Try all possible positions for the left parenthesis in the left part
        for i in range(len(left)):
            # Try all possible positions for the right parenthesis in the right part
            for j in range(1, len(right) + 1):
                # Split the left part into outer and inner parts
                left_outer = left[:i]
                left_inner = left[i:]
                
                # Split the right part into inner and outer parts
                right_inner = right[:j]
                right_outer = right[j:]
                
                # Calculate the value of the expression with the current positions of parentheses
                current_value = (int(left_inner) + int(right_inner))
                if left_outer:
                    current_value *= int(left_outer)
                if right_outer:
                    current_value *= int(right_outer)
                
                # Update the minimum value and the best positions if the current value is smaller
                if current_value < min_value:
                    min_value = current_value
                    best_left_pos = i
                    best_right_pos = j
        
        # Construct the result expression with the best positions of parentheses
        result = left[:best_left_pos] + '(' + left[best_left_pos:] + '+' + right[:best_right_pos] + ')' + right[best_right_pos:]
        
        return result

def minimizeResult(expression: str) -> str:
    return Solution().minimizeResult(expression)