import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_right
from itertools import accumulate

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        # Pair each monster's power with its corresponding coins
        monster_coin_pairs = list(zip(monsters, coins))
        
        # Sort the monster-coin pairs by monster power
        monster_coin_pairs.sort()
        
        # Extract the sorted monster powers and their cumulative coin sums
        sorted_monsters = [mc[0] for mc in monster_coin_pairs]
        cumulative_coins = list(accumulate(mc[1] for mc in monster_coin_pairs))
        
        # For each hero, find the maximum coins they can collect
        result = []
        for hero in heroes:
            # Find the position where this hero's power would fit in the sorted monster powers
            idx = bisect_right(sorted_monsters, hero)
            # If idx is 0, it means no monster can be defeated by this hero
            result.append(cumulative_coins[idx - 1] if idx > 0 else 0)
        
        return result

def maximumCoins(heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
    return Solution().maximumCoins(heroes, monsters, coins)