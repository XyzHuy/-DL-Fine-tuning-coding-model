import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        collisions = 0
        
        # Convert string to a list for easier manipulation
        dirs_list = list(directions)
        
        # Use two pointers to simulate the collisions
        left = 0
        right = n - 1
        
        # Move left pointer to find the first car that is not moving left
        while left < n and dirs_list[left] == 'L':
            left += 1
        
        # Move right pointer to find the first car that is not moving right
        while right >= 0 and dirs_list[right] == 'R':
            right -= 1
        
        # All cars between left and right pointers will collide
        # We need to count the number of 'R' and 'L' cars in this range
        for i in range(left, right + 1):
            if dirs_list[i] != 'S':
                collisions += 1
        
        return collisions

def countCollisions(directions: str) -> int:
    return Solution().countCollisions(directions)