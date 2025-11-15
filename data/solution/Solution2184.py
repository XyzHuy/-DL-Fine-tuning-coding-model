import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Generate all possible row configurations
        def generate_rows(width, bricks):
            rows = []
            def backtrack(position, current_row):
                if position == width:
                    # Convert current row to bitmask (excluding the last position)
                    bitmask = 0
                    for i in range(width - 1):
                        if current_row[i + 1] == 1:
                            bitmask |= (1 << i)
                    rows.append(bitmask)
                    return
                for brick in bricks:
                    if position + brick <= width:
                        current_row[position + brick] = 1
                        backtrack(position + brick, current_row)
                        current_row[position + brick] = 0
            current_row = [0] * (width + 1)
            current_row[0] = 1
            backtrack(0, current_row)
            return rows
        
        rows = generate_rows(width, bricks)
        
        # Check compatibility between rows
        def is_compatible(row1, row2):
            return (row1 & row2) == 0
        
        # Initialize DP table
        dp = [[0] * len(rows) for _ in range(height + 1)]
        for i in range(len(rows)):
            dp[1][i] = 1
        
        # Fill DP table
        for h in range(2, height + 1):
            for i in range(len(rows)):
                for j in range(len(rows)):
                    if is_compatible(rows[i], rows[j]):
                        dp[h][i] = (dp[h][i] + dp[h - 1][j]) % MOD
        
        # Sum up all ways to build a wall of height `height`
        result = sum(dp[height]) % MOD
        return result

def buildWall(height: int, width: int, bricks: List[int]) -> int:
    return Solution().buildWall(height, width, bricks)