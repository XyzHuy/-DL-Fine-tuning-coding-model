import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        size = n * m
        
        # Flatten the grid
        flat_grid = [grid[i][j] for i in range(n) for j in range(m)]
        
        # Calculate prefix products
        prefix_products = [1] * size
        for i in range(1, size):
            prefix_products[i] = (prefix_products[i - 1] * flat_grid[i - 1]) % MOD
        
        # Calculate suffix products
        suffix_products = [1] * size
        for i in range(size - 2, -1, -1):
            suffix_products[i] = (suffix_products[i + 1] * flat_grid[i + 1]) % MOD
        
        # Calculate the product matrix
        product_matrix_flat = [1] * size
        for i in range(size):
            product_matrix_flat[i] = (prefix_products[i] * suffix_products[i]) % MOD
        
        # Reshape the result back to a 2D list
        product_matrix = []
        index = 0
        for i in range(n):
            row = product_matrix_flat[index:index + m]
            product_matrix.append(row)
            index += m
        
        return product_matrix

def constructProductMatrix(grid: List[List[int]]) -> List[List[int]]:
    return Solution().constructProductMatrix(grid)