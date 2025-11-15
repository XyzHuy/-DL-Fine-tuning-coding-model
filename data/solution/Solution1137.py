import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize the first three Tribonacci numbers
        t0, t1, t2 = 0, 1, 1
        
        # Calculate the Tribonacci number for n
        for i in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next
        
        return t2

def tribonacci(n: int) -> int:
    return Solution().tribonacci(n)