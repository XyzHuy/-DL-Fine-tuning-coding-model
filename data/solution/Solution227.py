import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                # Integer division that truncates toward zero
                stack.append(int(stack.pop() / num))

        stack = []
        num = 0
        op = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            if char in '+-*/' or i == len(s) - 1:
                update(op, num)
                op = char
                num = 0

        return sum(stack)

def calculate(s: str) -> int:
    return Solution().calculate(s)