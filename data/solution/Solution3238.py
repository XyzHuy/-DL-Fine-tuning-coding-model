import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # Dictionary to count the number of balls each player picks of each color
        player_picks = defaultdict(lambda: defaultdict(int))
        
        # Count the balls picked by each player for each color
        for player, color in pick:
            player_picks[player][color] += 1
        
        # Set to keep track of winning players
        winning_players = set()
        
        # Check each player to see if they have won
        for player in range(n):
            for color, count in player_picks[player].items():
                if count >= player + 1:
                    winning_players.add(player)
                    break
        
        # Return the number of winning players
        return len(winning_players)

# Example usage:
# solution = Solution()
# print(solution.winningPlayerCount(4, [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))  # Output: 2
# print(solution.winningPlayerCount(5, [[1,1],[1,2],[1,3],[1,4]]))  # Output: 0
# print(solution.winningPlayerCount(5, [[1,1],[2,4],[2,4],[2,4]]))  # Output: 1

def winningPlayerCount(n: int, pick: List[List[int]]) -> int:
    return Solution().winningPlayerCount(n, pick)