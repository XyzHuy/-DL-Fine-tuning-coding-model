import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        from functools import lru_cache
        
        # Base case: if desiredTotal is 0, the first player wins
        if desiredTotal <= 0:
            return True
        
        # Calculate the total sum of numbers from 1 to maxChoosableInteger
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        
        # If the total sum is less than desiredTotal, the first player cannot win
        if total_sum < desiredTotal:
            return False
        
        # Use a bitmask to represent the state of the available numbers
        @lru_cache(None)
        def can_win(state, current_total):
            # Try each number from 1 to maxChoosableInteger
            for num in range(1, maxChoosableInteger + 1):
                # Create a bitmask for the current number
                mask = 1 << (num - 1)
                
                # Check if the number is available (not used yet)
                if state & mask == 0:
                    # If choosing this number makes the current_total >= desiredTotal
                    if current_total + num >= desiredTotal:
                        return True
                    
                    # Otherwise, check if the opponent cannot win in the next state
                    if not can_win(state | mask, current_total + num):
                        return True
            
            # If no move can force a win, return False
            return False
        
        # Start the game with an empty state (all numbers available) and current_total = 0
        return can_win(0, 0)

def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    return Solution().canIWin(maxChoosableInteger, desiredTotal)