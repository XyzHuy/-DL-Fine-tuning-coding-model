import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        # Calculate the total points for all levels
        total_points = sum(1 if x == 1 else -1 for x in possible)
        
        # Alice's points as she plays each level
        alice_points = 0
        
        # Iterate through the levels
        for i in range(len(possible) - 1):  # Alice must leave at least one level for Bob
            if possible[i] == 1:
                alice_points += 1
            else:
                alice_points -= 1
            
            # Bob's points will be the total points minus Alice's points
            bob_points = total_points - alice_points
            
            # Check if Alice has more points than Bob
            if alice_points > bob_points:
                return i + 1  # Return the number of levels Alice played
        
        # If no such level is found, return -1
        return -1

def minimumLevels(possible: List[int]) -> int:
    return Solution().minimumLevels(possible)