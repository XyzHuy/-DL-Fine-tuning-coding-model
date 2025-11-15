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
    def winningPlayer(self, x: int, y: int) -> str:
        turn = 0  # 0 for Alice, 1 for Bob
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            turn = 1 - turn  # Switch turn
        
        # If turn is 0, it means Bob made the last valid move, so Alice loses
        # If turn is 1, it means Alice made the last valid move, so Bob loses
        return "Alice" if turn == 1 else "Bob"

# Example usage:
# sol = Solution()
# print(sol.winningPlayer(2, 7))  # Output: "Alice"
# print(sol.winningPlayer(4, 11)) # Output: "Bob"

def winningPlayer(x: int, y: int) -> str:
    return Solution().winningPlayer(x, y)