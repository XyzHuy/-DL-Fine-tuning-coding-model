import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        refill_count = 0
        left = 0
        right = n - 1
        alice_water = capacityA
        bob_water = capacityB
        
        while left <= right:
            if left == right:
                if alice_water >= bob_water:
                    if alice_water < plants[left]:
                        refill_count += 1
                        alice_water = capacityA
                else:
                    if bob_water < plants[right]:
                        refill_count += 1
                        bob_water = capacityB
                alice_water -= plants[left]
            else:
                if alice_water < plants[left]:
                    refill_count += 1
                    alice_water = capacityA
                alice_water -= plants[left]
                
                if bob_water < plants[right]:
                    refill_count += 1
                    bob_water = capacityB
                bob_water -= plants[right]
            
            left += 1
            right -= 1
        
        return refill_count

def minimumRefill(plants: List[int], capacityA: int, capacityB: int) -> int:
    return Solution().minimumRefill(plants, capacityA, capacityB)