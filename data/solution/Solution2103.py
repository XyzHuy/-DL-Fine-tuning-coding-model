import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countPoints(self, rings: str) -> int:
        # Initialize a dictionary to keep track of colors on each rod
        rod_colors = {str(i): set() for i in range(10)}
        
        # Iterate over the rings string in steps of 2
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]
            # Add the color to the set of colors for the corresponding rod
            rod_colors[rod].add(color)
        
        # Count the number of rods that have all three colors
        count = sum(1 for colors in rod_colors.values() if len(colors) == 3)
        
        return count

def countPoints(rings: str) -> int:
    return Solution().countPoints(rings)