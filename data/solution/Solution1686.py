import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # Calculate the combined value of each stone for both players
        combined_values = [(aliceValues[i] + bobValues[i], i) for i in range(len(aliceValues))]
        
        # Sort the stones by their combined value in descending order
        combined_values.sort(reverse=True, key=lambda x: x[0])
        
        alice_score = 0
        bob_score = 0
        
        # Distribute the stones based on the sorted order
        for turn, (_, index) in enumerate(combined_values):
            if turn % 2 == 0:
                # Alice's turn
                alice_score += aliceValues[index]
            else:
                # Bob's turn
                bob_score += bobValues[index]
        
        # Determine the winner
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0

def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:
    return Solution().stoneGameVI(aliceValues, bobValues)