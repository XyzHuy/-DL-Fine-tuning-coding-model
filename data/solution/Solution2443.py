import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse_number(n: int) -> int:
            return int(str(n)[::-1])
        
        for i in range(num + 1):
            if i + reverse_number(i) == num:
                return True
        return False

def sumOfNumberAndReverse(num: int) -> bool:
    return Solution().sumOfNumberAndReverse(num)