import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            original_num = num
            while num > 0:
                digit = num % 10
                if digit == 0 or original_num % digit != 0:
                    return False
                num //= 10
            return True
        
        result = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
        
        return result

def selfDividingNumbers(left: int, right: int) -> List[int]:
    return Solution().selfDividingNumbers(left, right)