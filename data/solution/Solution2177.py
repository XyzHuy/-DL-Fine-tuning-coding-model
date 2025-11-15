import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # For three consecutive integers x-1, x, x+1 to sum to num:
        # (x-1) + x + (x+1) = num
        # 3x = num
        # x = num / 3
        # x must be an integer, so num must be divisible by 3
        if num % 3 == 0:
            x = num // 3
            return [x-1, x, x+1]
        else:
            return []

def sumOfThree(num: int) -> List[int]:
    return Solution().sumOfThree(num)