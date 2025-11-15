import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def can_partition(s: str, target: int) -> bool:
            if not s:
                return target == 0
            for i in range(1, len(s) + 1):
                if int(s[:i]) > target:
                    break
                if can_partition(s[i:], target - int(s[:i])):
                    return True
            return False
        
        def is_punishment_number(num: int) -> bool:
            return can_partition(str(num * num), num)
        
        punishment_sum = 0
        for i in range(1, n + 1):
            if is_punishment_number(i):
                punishment_sum += i * i
        
        return punishment_sum

def punishmentNumber(n: int) -> int:
    return Solution().punishmentNumber(n)