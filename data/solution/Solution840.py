import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(i: int, j: int) -> bool:
            # Check if the center is 5, a necessary condition for a 3x3 magic square with numbers 1-9
            if grid[i][j] != 5:
                return False
            
            # Define the relative positions of the numbers in a magic square
            magic_positions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            
            # Collect all numbers in the supposed magic square
            numbers = [grid[i + di][j + dj] for di, dj in magic_positions]
            numbers.append(5)  # Add the center number
            
            # Check if all numbers are distinct and between 1 and 9
            if sorted(numbers) != list(range(1, 10)):
                return False
            
            # Check the sums of rows, columns, and diagonals
            # Since the center is 5, we only need to check specific conditions
            return (grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] == 15 and  # top row
                    grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] == 15 and  # bottom row
                    grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1] == 15 and  # main diagonal
                    grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] == 15 and  # anti-diagonal
                    grid[i-1][j] + grid[i][j] + grid[i+1][j] == 15 and        # middle column
                    grid[i][j-1] + grid[i][j] + grid[i][j+1] == 15)         # middle row
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        # Iterate over all possible centers of 3x3 subgrids
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if is_magic_square(i, j):
                    count += 1
        
        return count

def numMagicSquaresInside(grid: List[List[int]]) -> int:
    return Solution().numMagicSquaresInside(grid)