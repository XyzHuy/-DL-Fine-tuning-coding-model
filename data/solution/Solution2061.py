import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(m)]
        cleaned = set()
        
        def is_within_bounds(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def is_clean(x, y):
            return (x, y) not in cleaned
        
        def can_move(x, y, dx, dy):
            nx, ny = x + dx, y + dy
            return is_within_bounds(nx, ny) and room[nx][ny] == 0
        
        def clean_room(x, y, d):
            if is_clean(x, y):
                cleaned.add((x, y))
            visited[x][y][d] = True
            
            dx, dy = directions[d]
            if can_move(x, y, dx, dy):
                clean_room(x + dx, y + dy, d)
            else:
                new_d = (d + 1) % 4
                if not visited[x][y][new_d]:
                    clean_room(x, y, new_d)
        
        clean_room(0, 0, 0)
        return len(cleaned)

def numberOfCleanRooms(room: List[List[int]]) -> int:
    return Solution().numberOfCleanRooms(room)