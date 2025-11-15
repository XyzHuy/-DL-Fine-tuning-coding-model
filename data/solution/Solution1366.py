import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Initialize a dictionary to store the ranking scores for each team
        ranking = defaultdict(lambda: [0] * len(votes[0]))
        
        # Count the votes for each team at each position
        for vote in votes:
            for i, team in enumerate(vote):
                ranking[team][i] -= 1  # Use negative values to sort in descending order later
        
        # Create a list of teams to sort
        teams = list(ranking.keys())
        
        # Sort the teams based on their ranking scores and then alphabetically
        teams.sort(key=lambda team: (ranking[team], team))
        
        # Join the sorted teams into a string
        return ''.join(teams)

def rankTeams(votes: List[str]) -> str:
    return Solution().rankTeams(votes)