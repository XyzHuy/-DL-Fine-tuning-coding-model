import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calculate_score(player: List[int]) -> int:
            score = 0
            strike = 0
            for pins in player:
                if strike > 0:
                    score += 2 * pins
                    strike -= 1
                else:
                    score += pins
                if pins == 10:
                    strike = 2
            return score
        
        score1 = calculate_score(player1)
        score2 = calculate_score(player2)
        
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0

def isWinner(player1: List[int], player2: List[int]) -> int:
    return Solution().isWinner(player1, player2)