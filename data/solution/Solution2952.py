import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        reachable = 0
        added_coins = 0
        i = 0
        
        while reachable < target:
            if i < len(coins) and coins[i] <= reachable + 1:
                reachable += coins[i]
                i += 1
            else:
                reachable += reachable + 1
                added_coins += 1
        
        return added_coins

def minimumAddedCoins(coins: List[int], target: int) -> int:
    return Solution().minimumAddedCoins(coins, target)