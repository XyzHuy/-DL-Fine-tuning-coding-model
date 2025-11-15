import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            operations += 1
        return operations

def countOperations(num1: int, num2: int) -> int:
    return Solution().countOperations(num1, num2)