import random
import functools
import collections
import string
import math
import datetime


import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        log_value = math.log(n, 3)
        rounded_log_value = round(log_value)
        return 3 ** rounded_log_value == n

def isPowerOfThree(n: int) -> bool:
    return Solution().isPowerOfThree(n)