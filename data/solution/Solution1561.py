import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort the piles in ascending order
        piles.sort()
        
        # Initialize the maximum coins you can have
        max_coins = 0
        
        # Iterate over the sorted piles, picking the second largest in each group of three
        for i in range(len(piles) // 3, len(piles), 2):
            max_coins += piles[i]
        
        return max_coins

def maxCoins(piles: List[int]) -> int:
    return Solution().maxCoins(piles)