import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort both players and trainers to use a two-pointer technique
        players.sort()
        trainers.sort()
        
        player_index = 0
        trainer_index = 0
        match_count = 0
        
        # Use two pointers to find matches
        while player_index < len(players) and trainer_index < len(trainers):
            if players[player_index] <= trainers[trainer_index]:
                # If the current player can be matched with the current trainer
                match_count += 1
                player_index += 1
                trainer_index += 1
            else:
                # If the current player cannot be matched with the current trainer
                trainer_index += 1
        
        return match_count

def matchPlayersAndTrainers(players: List[int], trainers: List[int]) -> int:
    return Solution().matchPlayersAndTrainers(players, trainers)