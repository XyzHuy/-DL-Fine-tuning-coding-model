import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # Sort the piles to make it easier to always take from the two largest piles
        piles = sorted([a, b, c])
        
        # Continue taking stones from the two largest piles until we can't make any more moves
        score = 0
        while len(piles) > 1 and piles[-1] > 0 and piles[-2] > 0:
            # Take one stone from the two largest piles
            piles[-1] -= 1
            piles[-2] -= 1
            score += 1
            # Re-sort the piles to maintain the order
            piles.sort()
        
        return score

# Example usage:
# sol = Solution()
# print(sol.maximumScore(2, 4, 6))  # Output: 6
# print(sol.maximumScore(4, 4, 6))  # Output: 7
# print(sol.maximumScore(1, 8, 8))  # Output: 8

def maximumScore(a: int, b: int, c: int) -> int:
    return Solution().maximumScore(a, b, c)