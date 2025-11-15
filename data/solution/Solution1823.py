import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize the position of the winner in a 0-based index
        winner_position = 0
        
        # Iterate from 2 to n to simulate the elimination process
        for i in range(2, n + 1):
            # Update the position of the winner
            winner_position = (winner_position + k) % i
        
        # Convert the 0-based index to a 1-based index
        return winner_position + 1

def findTheWinner(n: int, k: int) -> int:
    return Solution().findTheWinner(n, k)