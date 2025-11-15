import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        # Ensure digit1 is the smaller digit for easier generation
        if digit1 > digit2:
            digit1, digit2 = digit2, digit1
        
        # BFS approach to generate numbers with only digit1 and digit2
        from collections import deque
        
        queue = deque()
        if digit1 != 0:
            queue.append(digit1)
        if digit2 != 0:
            queue.append(digit2)
        
        max_32bit_int = 2**31 - 1
        
        while queue:
            current = queue.popleft()
            
            if current > max_32bit_int:
                continue
            
            if current > k and current % k == 0:
                return current
            
            # Generate the next numbers by appending digit1 and digit2
            if current * 10 + digit1 <= max_32bit_int:
                queue.append(current * 10 + digit1)
            if current * 10 + digit2 <= max_32bit_int:
                queue.append(current * 10 + digit2)
        
        return -1

def findInteger(k: int, digit1: int, digit2: int) -> int:
    return Solution().findInteger(k, digit1, digit2)