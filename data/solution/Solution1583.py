import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # Create a dictionary to store the pair of each friend
        pair_dict = {}
        for x, y in pairs:
            pair_dict[x] = y
            pair_dict[y] = x
        
        # Create a dictionary to store the preference rank of each friend for every other friend
        preference_rank = {i: {j: rank for rank, j in enumerate(prefs)} for i, prefs in enumerate(preferences)}
        
        unhappy_count = 0
        
        # Check each friend to see if they are unhappy
        for x in range(n):
            y = pair_dict[x]  # x's current pair
            x_prefers = preferences[x][:preferences[x].index(y)]  # Friends x prefers over y
            
            for u in x_prefers:
                v = pair_dict[u]  # u's current pair
                if preference_rank[u][x] < preference_rank[u][v]:  # u prefers x over v
                    unhappy_count += 1
                    break  # No need to check further for this x
        
        return unhappy_count

def unhappyFriends(n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
    return Solution().unhappyFriends(n, preferences, pairs)