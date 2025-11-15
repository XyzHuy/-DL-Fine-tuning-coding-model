import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ocean_view_buildings = []
        max_height = 0
        
        # Traverse the buildings from right to left
        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                ocean_view_buildings.append(i)
                max_height = heights[i]
        
        # The buildings are added in reverse order, so we need to reverse the list
        ocean_view_buildings.reverse()
        
        return ocean_view_buildings

def findBuildings(heights: List[int]) -> List[int]:
    return Solution().findBuildings(heights)