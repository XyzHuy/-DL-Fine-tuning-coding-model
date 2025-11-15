import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Create a set of all starting cities
        starting_cities = set(path[0] for path in paths)
        
        # The destination city will be the one that is not in the starting cities
        for path in paths:
            if path[1] not in starting_cities:
                return path[1]

def destCity(paths: List[List[str]]) -> str:
    return Solution().destCity(paths)