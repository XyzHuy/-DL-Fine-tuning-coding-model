import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # Define the jump requirements for the 3x3 grid
        jumps = {
            1: {3: 2, 7: 4, 9: 5},
            2: {8: 5},
            3: {1: 2, 7: 5, 9: 6},
            4: {6: 5},
            5: {},
            6: {4: 5},
            7: {1: 4, 3: 5, 9: 8},
            8: {2: 5},
            9: {1: 5, 3: 6, 7: 8}
        }
        
        def dfs(current, visited, length):
            if length == n:
                return 1
            count = 1 if length >= m else 0
            for next in range(1, 10):
                if next not in visited:
                    jump = jumps[current].get(next)
                    if jump is None or jump in visited:
                        visited.add(next)
                        count += dfs(next, visited, length + 1)
                        visited.remove(next)
            return count
        
        # Start from each of the 9 keys and calculate the number of patterns
        return dfs(1, {1}, 1) * 4 + dfs(2, {2}, 1) * 4 + dfs(5, {5}, 1)

def numberOfPatterns(m: int, n: int) -> int:
    return Solution().numberOfPatterns(m, n)