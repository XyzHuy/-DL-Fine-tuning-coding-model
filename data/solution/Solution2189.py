import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def houseOfCards(self, n: int) -> int:
        # memoization dictionary to store the number of ways to build a house with a given number of cards and max base width
        memo = {}

        def dp(cards_left, max_base_width):
            if (cards_left, max_base_width) in memo:
                return memo[(cards_left, max_base_width)]
            
            if cards_left < 0:
                return 0
            
            if cards_left == 0:
                return 1
            
            count = 0
            # Try to place 1 to max_base_width triangles in the next row
            for triangles in range(1, max_base_width):
                # Cards needed for the current row
                cards_needed = 2 * triangles + (triangles - 1)
                if cards_needed > cards_left:
                    break
                # Recur for the remaining cards and reduced base width
                count += dp(cards_left - cards_needed, triangles)
            
            memo[(cards_left, max_base_width)] = count
            return count
        
        # Start with n cards and the maximum base width which is n//2 + 1 (since each triangle needs 2 cards and 1 horizontal card between them)
        return dp(n, n // 2 + 1)

def houseOfCards(n: int) -> int:
    return Solution().houseOfCards(n)