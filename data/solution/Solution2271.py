import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()  # Ensure tiles are sorted by their starting positions
        max_covered = 0
        right = 0
        current_covered = 0
        
        for left in range(len(tiles)):
            # Move the right pointer to find the farthest tile segment the carpet can cover
            while right < len(tiles) and tiles[right][0] + carpetLen > tiles[left][0]:
                if tiles[right][1] < tiles[left][0] + carpetLen:
                    # The entire segment is covered
                    current_covered += tiles[right][1] - tiles[right][0] + 1
                    right += 1
                else:
                    # Only part of the segment is covered
                    overlap = (tiles[left][0] + carpetLen - tiles[right][0])
                    max_covered = max(max_covered, current_covered + overlap)
                    break
            
            # Update the maximum number of tiles covered
            max_covered = max(max_covered, current_covered)
            
            # Move the left pointer to the next tile segment
            if right > left:
                current_covered -= (tiles[left][1] - tiles[left][0] + 1)
        
        return max_covered

def maximumWhiteTiles(tiles: List[List[int]], carpetLen: int) -> int:
    return Solution().maximumWhiteTiles(tiles, carpetLen)