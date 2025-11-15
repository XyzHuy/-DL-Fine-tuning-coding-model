import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def evaluate(self, expression: str) -> int:
        def get_val(val, scope):
            return scope.get(val, val)
        
        def parse(tokens, index, scope):
            if tokens[index] != '(':
                val = get_val(tokens[index], scope)
                return int(val), index
            
            op = tokens[index + 1]
            if op == 'add':
                val1, index = parse(tokens, index + 2, scope)
                val2, index = parse(tokens, index + 1, scope)
                return val1 + val2, index + 1
            elif op == 'mult':
                val1, index = parse(tokens, index + 2, scope)
                val2, index = parse(tokens, index + 1, scope)
                return val1 * val2, index + 1
            else:  # op == 'let'
                new_scope = scope.copy()
                i = index + 2
                while i < len(tokens) and tokens[i] != '(' and tokens[i + 1] != ')':
                    var = tokens[i]
                    val, i = parse(tokens, i + 1, new_scope)
                    new_scope[var] = val
                    i += 1
                val, index = parse(tokens, i, new_scope)
                return val, index + 1
        
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        return parse(tokens, 0, {})[0]

def evaluate(expression: str) -> int:
    return Solution().evaluate(expression)