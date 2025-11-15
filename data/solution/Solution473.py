import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        if n < 4:
            return False
        
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        
        side_length = perimeter // 4
        matchsticks.sort(reverse=True)  # Sort in descending order to optimize backtracking
        
        # Try to partition the matchsticks into 4 subsets, each with sum equal to side_length
        def dfs(index, current_sides):
            if index == n:
                return all(side == side_length for side in current_sides)
            
            for i in range(4):
                if current_sides[i] + matchsticks[index] <= side_length:
                    current_sides[i] += matchsticks[index]
                    if dfs(index + 1, current_sides):
                        return True
                    current_sides[i] -= matchsticks[index]
                
                # If the current side is 0, no need to try other sides
                if current_sides[i] == 0:
                    break
            
            return False
        
        return dfs(0, [0] * 4)

def makesquare(matchsticks: List[int]) -> bool:
    return Solution().makesquare(matchsticks)