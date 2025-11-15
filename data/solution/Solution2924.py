import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Initialize a set to keep track of all teams that have incoming edges
        has_incoming_edge = set()
        
        # Populate the set with all nodes that have incoming edges
        for u, v in edges:
            has_incoming_edge.add(v)
        
        # The champion will be the node with no incoming edges
        champions = [i for i in range(n) if i not in has_incoming_edge]
        
        # If there is exactly one such node, it is the champion
        if len(champions) == 1:
            return champions[0]
        else:
            return -1

def findChampion(n: int, edges: List[List[int]]) -> int:
    return Solution().findChampion(n, edges)