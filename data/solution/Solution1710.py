import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the box types by the number of units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        for numberOfBoxes, unitsPerBox in boxTypes:
            if truckSize == 0:
                break
            # Load as many boxes of this type as possible
            boxes_to_load = min(numberOfBoxes, truckSize)
            total_units += boxes_to_load * unitsPerBox
            truckSize -= boxes_to_load
        
        return total_units

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    return Solution().maximumUnits(boxTypes, truckSize)