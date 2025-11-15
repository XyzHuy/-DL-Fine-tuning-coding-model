import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Helper function to perform the arithmetic operation
        def compute(left, right, operator):
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
        
        # Base case: if the expression is a number, return it as the only result
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        # Iterate through the expression to find operators
        for i in range(len(expression)):
            if expression[i] in "+-*":
                # Split the expression into left and right parts
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results from the left and right parts using the current operator
                for left in left_results:
                    for right in right_results:
                        results.append(compute(left, right, expression[i]))
        
        return results

def diffWaysToCompute(expression: str) -> List[int]:
    return Solution().diffWaysToCompute(expression)