import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        def neighbors(x, y):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    yield nx, ny

        def dfs(x, y, region_id):
            if (x, y) in visited:
                return
            visited.add((x, y))
            regions[region_id].add((x, y))
            for nx, ny in neighbors(x, y):
                if isInfected[nx][ny] == 1:
                    dfs(nx, ny, region_id)
                elif isInfected[nx][ny] == 0:
                    threatened[region_id].add((nx, ny))
                    walls_needed[region_id] += 1

        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0

        while True:
            regions = []
            threatened = []
            walls_needed = []
            visited = set()

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        regions.append(set())
                        threatened.append(set())
                        walls_needed.append(0)
                        dfs(i, j, len(regions) - 1)

            if not regions:
                break

            # Find the region that threatens the most uninfected cells
            max_threatened = max(range(len(threatened)), key=lambda i: len(threatened[i]))

            # Build walls around the most threatening region
            total_walls += walls_needed[max_threatened]
            for i, region in enumerate(regions):
                if i == max_threatened:
                    # Contain this region
                    for x, y in region:
                        isInfected[x][y] = -1
                else:
                    # Spread the virus to the threatened cells
                    for x, y in threatened[i]:
                        isInfected[x][y] = 1

        return total_walls

def containVirus(isInfected: List[List[int]]) -> int:
    return Solution().containVirus(isInfected)