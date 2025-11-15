import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(cells: List[int]) -> List[int]:
            # The first and last cells will be vacant after the first day
            next_cells = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    next_cells[i] = 1
            return next_cells
        
        # Dictionary to store the state and the corresponding day
        seen_states = {}
        current_state = cells[:]
        
        # Simulate the days
        for day in range(n):
            # Convert the current state to a tuple to use as a dictionary key
            current_state_tuple = tuple(current_state)
            if current_state_tuple in seen_states:
                # Cycle detected
                cycle_length = day - seen_states[current_state_tuple]
                # Skip full cycles and compute the state for the remaining days
                remaining_days = (n - day) % cycle_length
                return self.prisonAfterNDays(current_state, remaining_days)
            else:
                # Store the day we first saw this state
                seen_states[current_state_tuple] = day
                # Move to the next day
                current_state = next_day(current_state)
        
        return current_state

def prisonAfterNDays(cells: List[int], n: int) -> List[int]:
    return Solution().prisonAfterNDays(cells, n)