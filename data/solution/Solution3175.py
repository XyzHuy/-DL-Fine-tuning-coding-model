import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        k = min(k, n - 1)  # No need to go beyond n-1 as the winner will be determined within n-1 comparisons
        i = cnt = 0  # i is the index of the current winner, cnt is the count of consecutive wins
        
        for j in range(1, n):
            if skills[i] < skills[j]:
                i = j  # Update the winner to the current player
                cnt = 1  # Reset the count of consecutive wins
            else:
                cnt += 1  # Increment the count of consecutive wins for the current winner
            
            if cnt == k:
                break  # If the current winner has won k consecutive games, break the loop
        
        return i  # Return the index of the winning player

def findWinningPlayer(skills: List[int], k: int) -> int:
    return Solution().findWinningPlayer(skills, k)