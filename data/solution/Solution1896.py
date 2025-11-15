import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def evaluate_and_cost(expr):
            # Base case: single digit
            if expr.isdigit():
                return int(expr), 1  # value, cost to flip
            
            # Evaluate the expression using stack to handle parentheses
            stack_val = []
            stack_op = []
            i = 0
            while i < len(expr):
                if expr[i] == '(':
                    j = i + 1
                    open_count = 1
                    while j < len(expr):
                        if expr[j] == '(':
                            open_count += 1
                        elif expr[j] == ')':
                            open_count -= 1
                        if open_count == 0:
                            break
                        j += 1
                    val, cost = evaluate_and_cost(expr[i + 1:j])
                    stack_val.append(val)
                    stack_op.append(cost)
                    i = j
                elif expr[i] in '01':
                    stack_val.append(int(expr[i]))
                    stack_op.append(1)
                else:
                    stack_op.append(expr[i])
                i += 1
            
            # Now stack_val contains values and stack_op contains costs and operators
            i = 0
            while len(stack_val) > 1:
                val1 = stack_val.pop(0)
                cost1 = stack_op.pop(0)
                op = stack_op.pop(0)
                val2 = stack_val.pop(0)
                cost2 = stack_op.pop(0)
                
                if op == '&':
                    new_val = val1 & val2
                    if val1 == val2 == 1:  # Both are 1, changing any to 0 flips the result
                        new_cost = min(cost1, cost2)
                    elif val1 == val2 == 0:  # Both are 0, changing '&' to '|' and any 0 to 1 flips the result
                        new_cost = min(cost1, cost2) + 1
                    else:  # One is 0 and the other is 1, changing '&' to '|' flips the result
                        new_cost = 1
                elif op == '|':
                    new_val = val1 | val2
                    if val1 == val2 == 1:  # Both are 1, changing '|' to '&' and any 1 to 0 flips the result
                        new_cost = min(cost1, cost2) + 1
                    elif val1 == val2 == 0:  # Both are 0, changing any to 1 flips the result
                        new_cost = min(cost1, cost2)
                    else:  # One is 1 and the other is 0, changing '|' to '&' flips the result
                        new_cost = 1
                
                stack_val.insert(0, new_val)
                stack_op.insert(0, new_cost)
            
            return stack_val[0], stack_op[0]
        
        final_value, min_cost_to_flip = evaluate_and_cost(expression)
        return min_cost_to_flip

def minOperationsToFlip(expression: str) -> int:
    return Solution().minOperationsToFlip(expression)