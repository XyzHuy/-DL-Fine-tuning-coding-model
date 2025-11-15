import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        
        # A valid parentheses string must have even length
        if n % 2 != 0:
            return False
        
        # Initialize counters for flexible and locked parentheses
        flexible = 0
        locked_open = 0
        
        # Traverse the string from left to right
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    locked_open += 1
                else:
                    # If we encounter a locked closing parenthesis, try to match it
                    if locked_open > 0:
                        locked_open -= 1
                    elif flexible > 0:
                        flexible -= 1
                    else:
                        # No way to match this closing parenthesis
                        return False
            else:
                # Flexible can be either '(' or ')'
                flexible += 1
        
        # Traverse the string from right to left to ensure we can match all locked '('
        flexible = 0
        locked_close = 0
        
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    locked_close += 1
                else:
                    # If we encounter a locked opening parenthesis, try to match it
                    if locked_close > 0:
                        locked_close -= 1
                    elif flexible > 0:
                        flexible -= 1
                    else:
                        # No way to match this opening parenthesis
                        return False
            else:
                # Flexible can be either '(' or ')'
                flexible += 1
        
        return True

def canBeValid(s: str, locked: str) -> bool:
    return Solution().canBeValid(s, locked)