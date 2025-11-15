import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(maze), len(maze[0])
        start, destination = tuple(start), tuple(destination)
        # Priority queue to store the (distance, x, y) tuples
        pq = [(0, start[0], start[1])]
        # Set to keep track of visited positions
        visited = set()
        
        while pq:
            dist, x, y = heapq.heappop(pq)
            if (x, y) == destination:
                return dist
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y, count = x, y, 0
                # Roll the ball until it hits a wall
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                # If the new position is not visited, add it to the priority queue
                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, new_x, new_y))
        
        return -1

def shortestDistance(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    return Solution().shortestDistance(maze, start, destination)