import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target_skill = skill[0] + skill[-1]
        chemistry_sum = 0
        
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target_skill:
                return -1
            chemistry_sum += skill[i] * skill[n - 1 - i]
        
        return chemistry_sum

def dividePlayers(skill: List[int]) -> int:
    return Solution().dividePlayers(skill)