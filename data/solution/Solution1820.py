import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        matched_girls = [-1] * n  # matched_girls[j] = i means the j-th girl is matched with the i-th boy

        def can_match(boy, visited):
            for girl in range(n):
                if grid[boy][girl] == 1 and not visited[girl]:
                    visited[girl] = True
                    if matched_girls[girl] == -1 or can_match(matched_girls[girl], visited):
                        matched_girls[girl] = boy
                        return True
            return False

        max_invitations = 0
        for boy in range(m):
            visited = [False] * n
            if can_match(boy, visited):
                max_invitations += 1

        return max_invitations

def maximumInvitations(grid: List[List[int]]) -> int:
    return Solution().maximumInvitations(grid)