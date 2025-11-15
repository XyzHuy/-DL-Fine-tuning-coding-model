import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Function to get all elements of the current layer
        def get_layer_elements(grid, layer):
            top = layer
            bottom = m - layer - 1
            left = layer
            right = n - layer - 1
            
            elements = []
            
            # Traverse from left to right along the top row
            for col in range(left, right):
                elements.append(grid[top][col])
            
            # Traverse from top to bottom along the right column
            for row in range(top, bottom):
                elements.append(grid[row][right])
            
            # Traverse from right to left along the bottom row
            for col in range(right, left, -1):
                elements.append(grid[bottom][col])
            
            # Traverse from bottom to top along the left column
            for row in range(bottom, top, -1):
                elements.append(grid[row][left])
            
            return elements
        
        # Function to set elements back into the current layer
        def set_layer_elements(grid, layer, elements):
            top = layer
            bottom = m - layer - 1
            left = layer
            right = n - layer - 1
            
            index = 0
            
            # Traverse from left to right along the top row
            for col in range(left, right):
                grid[top][col] = elements[index]
                index += 1
            
            # Traverse from top to bottom along the right column
            for row in range(top, bottom):
                grid[row][right] = elements[index]
                index += 1
            
            # Traverse from right to left along the bottom row
            for col in range(right, left, -1):
                grid[bottom][col] = elements[index]
                index += 1
            
            # Traverse from bottom to top along the left column
            for row in range(bottom, top, -1):
                grid[row][left] = elements[index]
                index += 1
        
        # Number of layers
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            elements = get_layer_elements(grid, layer)
            num_elements = len(elements)
            rotated_elements = elements[k % num_elements:] + elements[:k % num_elements]
            set_layer_elements(grid, layer, rotated_elements)
        
        return grid

def rotateGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    return Solution().rotateGrid(grid, k)