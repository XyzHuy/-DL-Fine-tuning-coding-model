import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # Calculate the difference in rewards for each type of cheese
        differences = [(r1 - r2) for r1, r2 in zip(reward1, reward2)]
        
        # Sort the differences in descending order
        differences.sort(reverse=True)
        
        # The first mouse should eat the k types of cheese with the highest difference
        max_points = sum(reward2) + sum(differences[:k])
        
        return max_points

def miceAndCheese(reward1: List[int], reward2: List[int], k: int) -> int:
    return Solution().miceAndCheese(reward1, reward2, k)