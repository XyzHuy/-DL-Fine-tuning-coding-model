import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canWin(self, currentState: str) -> bool:
        def canWinHelper(state, memo):
            if state in memo:
                return memo[state]
            
            for i in range(len(state) - 1):
                if state[i] == '+' and state[i + 1] == '+':
                    new_state = state[:i] + '--' + state[i + 2:]
                    if not canWinHelper(new_state, memo):
                        memo[state] = True
                        return True
            
            memo[state] = False
            return False
        
        memo = {}
        return canWinHelper(currentState, memo)

def canWin(currentState: str) -> bool:
    return Solution().canWin(currentState)