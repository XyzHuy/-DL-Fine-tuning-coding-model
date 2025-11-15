import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        # We start with one 'A' on the screen and no characters copied
        current_chars = 1
        copied_chars = 0
        operations = 0
        
        while current_chars < n:
            # If we can copy and paste to reach a multiple of n, do so
            if n % current_chars == 0:
                copied_chars = current_chars
                operations += 1  # Copy All
            current_chars += copied_chars
            operations += 1  # Paste
        
        return operations

def minSteps(n: int) -> int:
    return Solution().minSteps(n)