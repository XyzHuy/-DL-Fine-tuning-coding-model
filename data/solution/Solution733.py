import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the original color of the starting pixel
        original_color = image[sr][sc]
        
        # If the original color is the same as the new color, no need to do anything
        if original_color == color:
            return image
        
        # Define the directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Helper function to perform DFS
        def dfs(r: int, c: int):
            # Change the color of the current pixel
            image[r][c] = color
            
            # Explore the neighboring pixels
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check if the neighboring pixel is within bounds and has the original color
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_color:
                    dfs(nr, nc)
        
        # Start the DFS from the starting pixel
        dfs(sr, sc)
        
        return image

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    return Solution().floodFill(image, sr, sc, color)