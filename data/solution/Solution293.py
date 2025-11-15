import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        possible_states = []
        for i in range(len(currentState) - 1):
            if currentState[i:i+2] == "++":
                new_state = currentState[:i] + "--" + currentState[i+2:]
                possible_states.append(new_state)
        return possible_states

def generatePossibleNextMoves(currentState: str) -> List[str]:
    return Solution().generatePossibleNextMoves(currentState)