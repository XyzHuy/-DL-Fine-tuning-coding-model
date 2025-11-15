import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # Function to get the minimum squares needed to tile the rectangle with given height profile
        def backtrack(heights, moves):
            nonlocal min_squares
            # Check if the current configuration is already the minimum
            if moves >= min_squares:
                return
            # Check if the rectangle is fully tiled
            if all(h == n for h in heights):
                min_squares = moves
                return
            
            # Find the position of the first column with the minimum height
            min_height = min(heights)
            idx = heights.index(min_height)
            # Find the width of the rectangle that can be filled starting from idx
            j = idx
            while j < m and heights[j] == min_height:
                j += 1
            
            # Try placing squares of different sizes
            for size in range(1, min(j - idx, n - min_height) + 1):
                # Update the height profile for the current square placement
                new_heights = heights[:]
                for k in range(idx, idx + size):
                    new_heights[k] += size
                # Recur with the new height profile
                backtrack(new_heights, moves + 1)
        
        # Initialize the minimum number of squares to a large number
        min_squares = float('inf')
        # Start backtracking with an initial height profile of all zeros
        backtrack([0] * m, 0)
        return min_squares

# Example usage:
# sol = Solution()
# print(sol.tilingRectangle(2, 3))  # Output: 3
# print(sol.tilingRectangle(5, 8))  # Output: 5
# print(sol.tilingRectangle(11, 13))  # Output: 6

def tilingRectangle(n: int, m: int) -> int:
    return Solution().tilingRectangle(n, m)