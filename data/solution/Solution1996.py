import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort the properties: first by attack in descending order, then by defense in ascending order
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        max_defense = 0
        weak_count = 0
        
        for _, defense in properties:
            if defense < max_defense:
                weak_count += 1
            else:
                max_defense = defense
        
        return weak_count

def numberOfWeakCharacters(properties: List[List[int]]) -> int:
    return Solution().numberOfWeakCharacters(properties)