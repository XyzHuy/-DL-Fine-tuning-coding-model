import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        # Calculate the Nim-sum (XOR of all pile sizes)
        nim_sum = 0
        for pile in piles:
            nim_sum ^= pile
        
        # If the Nim-sum is non-zero, Alice wins; otherwise, Bob wins
        return nim_sum != 0

def nimGame(piles: List[int]) -> bool:
    return Solution().nimGame(piles)