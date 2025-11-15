import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Calculate the number of states each pig can be in
        states_per_pig = minutesToTest // minutesToDie + 1
        
        # Find the minimum number of pigs needed
        pigs = 0
        while states_per_pig ** pigs < buckets:
            pigs += 1
        
        return pigs

def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    return Solution().poorPigs(buckets, minutesToDie, minutesToTest)