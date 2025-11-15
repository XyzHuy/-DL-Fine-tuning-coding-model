import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        
        m, n = len(targetGrid), len(targetGrid[0])
        color_bounds = defaultdict(lambda: [m, -1, n, -1])  # top, bottom, left, right
        colors = set()
        
        # Determine the bounding box for each color
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                colors.add(color)
                color_bounds[color][0] = min(color_bounds[color][0], i)
                color_bounds[color][1] = max(color_bounds[color][1], i)
                color_bounds[color][2] = min(color_bounds[color][2], j)
                color_bounds[color][3] = max(color_bounds[color][3], j)
        
        # Check if a color can be printed without overlapping other colors
        def can_print(color):
            top, bottom, left, right = color_bounds[color]
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    if targetGrid[i][j] != color and targetGrid[i][j] != 0:
                        return False
            return True
        
        # Remove a color from the grid
        def remove_color(color):
            top, bottom, left, right = color_bounds[color]
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    if targetGrid[i][j] == color:
                        targetGrid[i][j] = 0
        
        # Topological sort to ensure we print colors in the correct order
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        
        for color in colors:
            top, bottom, left, right = color_bounds[color]
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    if targetGrid[i][j] != color:
                        in_degree[color] += 1
                        graph[targetGrid[i][j]].append(color)
        
        # Kahn's algorithm for topological sorting
        queue = deque([color for color in colors if in_degree[color] == 0])
        printed_colors = set()
        
        while queue:
            color = queue.popleft()
            printed_colors.add(color)
            if not can_print(color):
                return False
            remove_color(color)
            for neighbor in graph[color]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(printed_colors) == len(colors)

def isPrintable(targetGrid: List[List[int]]) -> bool:
    return Solution().isPrintable(targetGrid)