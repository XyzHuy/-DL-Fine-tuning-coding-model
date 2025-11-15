import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        stack = []
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If there are still digits to remove, remove them from the end
        final_stack = stack[:-k] if k else stack
        
        # Join the result and remove leading zeros
        result = ''.join(final_stack).lstrip('0')
        
        # If the result is empty, return "0"
        return result if result else "0"

def removeKdigits(num: str, k: int) -> str:
    return Solution().removeKdigits(num, k)