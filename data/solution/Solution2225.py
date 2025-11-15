import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Dictionary to keep track of the number of losses for each player
        loss_count = defaultdict(int)
        
        # Set to keep track of all players who have played at least one match
        players = set()
        
        # Process each match
        for winner, loser in matches:
            loss_count[loser] += 1
            players.add(winner)
            players.add(loser)
        
        # List of players with no losses
        no_losses = [player for player in players if loss_count[player] == 0]
        
        # List of players with exactly one loss
        one_loss = [player for player, count in loss_count.items() if count == 1]
        
        # Return the sorted lists
        return [sorted(no_losses), sorted(one_loss)]

def findWinners(matches: List[List[int]]) -> List[List[int]]:
    return Solution().findWinners(matches)