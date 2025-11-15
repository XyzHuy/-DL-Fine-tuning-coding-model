import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0
        
        for i in range(len(num_str) - k + 1):
            substring = num_str[i:i+k]
            divisor = int(substring)
            if divisor != 0 and num % divisor == 0:
                count += 1
                
        return count

def divisorSubstrings(num: int, k: int) -> int:
    return Solution().divisorSubstrings(num, k)