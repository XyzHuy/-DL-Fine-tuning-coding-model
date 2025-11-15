import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # Calculate the total damage without using armor
        total_damage = sum(damage)
        
        # Find the maximum damage in a single level
        max_damage = max(damage)
        
        # Use the armor to mitigate the maximum damage
        # The effective damage reduction is the minimum of max_damage and armor
        effective_armor = min(max_damage, armor)
        
        # The minimum health needed is the total damage minus the effective armor plus 1
        return total_damage - effective_armor + 1

def minimumHealth(damage: List[int], armor: int) -> int:
    return Solution().minimumHealth(damage, armor)