import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        
        # Queues to hold the indices of Radiant and Dire senators
        radiant = deque()
        dire = deque()
        
        # Initialize the queues with the indices of the senators
        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Process the voting rounds
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # The senator with the smaller index bans the other
            if r_index < d_index:
                radiant.append(r_index + len(senate))
            else:
                dire.append(d_index + len(senate))
        
        # The party with remaining senators wins
        return "Radiant" if radiant else "Dire"

def predictPartyVictory(senate: str) -> str:
    return Solution().predictPartyVictory(senate)