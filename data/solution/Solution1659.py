import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # Constants for the happiness values
        INTROVERT_BASE = 120
        EXTROVERT_BASE = 40
        INTROVERT_PENALTY = 30
        EXTROVERT_BONUS = 20
        
        # Calculate the happiness change for two adjacent people
        def happiness_diff(a, b):
            if a == 0 or b == 0:
                return 0
            if a == b == 1:
                return -30 - 30
            if a == b == 2:
                return 20 + 20
            return -30 + 20
        
        # Function to calculate the total happiness for a given state
        def total_happiness(state, row, col):
            total = 0
            for i in range(m):
                for j in range(n):
                    person = state[i * n + j]
                    if person == 0:
                        continue
                    total += INTROVERT_BASE if person == 1 else EXTROVERT_BASE
                    # Check north neighbor
                    if i > 0:
                        total += happiness_diff(person, state[(i - 1) * n + j])
                    # Check west neighbor
                    if j > 0:
                        total += happiness_diff(person, state[i * n + j - 1])
            return total
        
        # DFS with memoization to try all possible placements
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(row, col, introverts, extroverts, prev_row):
            if introverts == 0 and extroverts == 0 or row == m:
                return 0
            
            max_happiness = 0
            if col == n:
                max_happiness = dfs(row + 1, 0, introverts, extroverts, prev_row)
            else:
                # Try placing nothing
                max_happiness = dfs(row, col + 1, introverts, extroverts, prev_row[1:] + (0,))
                # Try placing an introvert
                if introverts > 0:
                    new_state = prev_row[1:] + (1,)
                    current_happiness = (INTROVERT_BASE 
                                         + happiness_diff(1, prev_row[0]) 
                                         + (happiness_diff(1, prev_row[-1]) if col > 0 else 0))
                    max_happiness = max(max_happiness, 
                                        current_happiness + dfs(row, col + 1, introverts - 1, extroverts, new_state))
                # Try placing an extrovert
                if extroverts > 0:
                    new_state = prev_row[1:] + (2,)
                    current_happiness = (EXTROVERT_BASE 
                                         + happiness_diff(2, prev_row[0]) 
                                         + (happiness_diff(2, prev_row[-1]) if col > 0 else 0))
                    max_happiness = max(max_happiness, 
                                        current_happiness + dfs(row, col + 1, introverts, extroverts - 1, new_state))
            
            return max_happiness
        
        return dfs(0, 0, introvertsCount, extrovertsCount, tuple([0] * n))

def getMaxGridHappiness(m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
    return Solution().getMaxGridHappiness(m, n, introvertsCount, extrovertsCount)