import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = -1
        best_coordinate = (0, 0)
        
        # Iterate over all possible coordinates in the range of the towers
        for x in range(51):
            for y in range(51):
                current_quality = 0
                for tower in towers:
                    xi, yi, qi = tower
                    distance = math.sqrt((xi - x) ** 2 + (yi - y) ** 2)
                    if distance <= radius:
                        current_quality += math.floor(qi / (1 + distance))
                
                # Update the best coordinate if the current one has higher quality
                if current_quality > max_quality:
                    max_quality = current_quality
                    best_coordinate = (x, y)
                # If quality is the same, choose the lexicographically smaller coordinate
                elif current_quality == max_quality:
                    if (x, y) < best_coordinate:
                        best_coordinate = (x, y)
        
        return list(best_coordinate)

def bestCoordinate(towers: List[List[int]], radius: int) -> List[int]:
    return Solution().bestCoordinate(towers, radius)