import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for x in asteroids:
            if x > 0:
                stk.append(x)
            else:
                while stk and stk[-1] > 0 and stk[-1] < -x:
                    stk.pop()
                if stk and stk[-1] == -x:
                    stk.pop()
                elif not stk or stk[-1] < 0:
                    stk.append(x)
        return stk

def asteroidCollision(asteroids: List[int]) -> List[int]:
    return Solution().asteroidCollision(asteroids)