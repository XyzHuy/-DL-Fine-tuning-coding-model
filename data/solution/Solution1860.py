import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while True:
            if memory1 >= memory2:
                if memory1 >= i:
                    memory1 -= i
                else:
                    return [i, memory1, memory2]
            else:
                if memory2 >= i:
                    memory2 -= i
                else:
                    return [i, memory1, memory2]
            i += 1

def memLeak(memory1: int, memory2: int) -> List[int]:
    return Solution().memLeak(memory1, memory2)