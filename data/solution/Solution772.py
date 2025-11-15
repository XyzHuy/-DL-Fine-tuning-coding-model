import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0
            
            while len(s) > 0:
                char = s.pop(0)
                
                if char.isdigit():
                    num = num * 10 + int(char)
                
                if char == '(':
                    num = helper(s)
                
                if (not char.isdigit() and not char.isspace()) or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop() / num))  # Truncate toward zero
                    
                    sign = char
                    num = 0
                
                if char == ')':
                    break
            
            return sum(stack)
        
        # Convert string to list for easier manipulation
        return helper(list(s))

def calculate(s: str) -> int:
    return Solution().calculate(s)