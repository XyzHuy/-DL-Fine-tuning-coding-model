import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]:
            return 0
        ans = 0
        for i in range(len(enemyEnergies) - 1, -1, -1):
            ans += currentEnergy // enemyEnergies[0]
            currentEnergy %= enemyEnergies[0]
            currentEnergy += enemyEnergies[i]
        return ans

def maximumPoints(enemyEnergies: List[int], currentEnergy: int) -> int:
    return Solution().maximumPoints(enemyEnergies, currentEnergy)