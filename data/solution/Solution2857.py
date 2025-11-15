import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        count = 0
        coord_dict = defaultdict(int)
        
        for x, y in coordinates:
            for i in range(k + 1):
                x1, y1 = x ^ i, y ^ (k - i)
                if (x1, y1) in coord_dict:
                    count += coord_dict[(x1, y1)]
            coord_dict[(x, y)] += 1
        
        return count

def countPairs(coordinates: List[List[int]], k: int) -> int:
    return Solution().countPairs(coordinates, k)