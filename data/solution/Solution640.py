import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expression):
            tokens = expression.replace('+', '#+').replace('-', '#-').split('#')
            x_coeff = 0
            const = 0
            for token in tokens:
                if not token:
                    continue
                if token == 'x' or token == '+x':
                    x_coeff += 1
                elif token == '-x':
                    x_coeff -= 1
                elif 'x' in token:
                    x_coeff += int(token[:token.index('x')])
                else:
                    const += int(token)
            return x_coeff, const

        left_expr, right_expr = equation.split('=')
        left_x, left_const = parse(left_expr)
        right_x, right_const = parse(right_expr)

        total_x = left_x - right_x
        total_const = right_const - left_const

        if total_x == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={total_const // total_x}"

def solveEquation(equation: str) -> str:
    return Solution().solveEquation(equation)