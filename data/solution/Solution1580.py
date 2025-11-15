import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # Sort the boxes in non-decreasing order
        boxes.sort()
        
        # Create a list to store the minimum height from the left to each position
        left_min = [0] * len(warehouse)
        left_min[0] = warehouse[0]
        for i in range(1, len(warehouse)):
            left_min[i] = min(left_min[i - 1], warehouse[i])
        
        # Create a list to store the minimum height from the right to each position
        right_min = [0] * len(warehouse)
        right_min[-1] = warehouse[-1]
        for i in range(len(warehouse) - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], warehouse[i])
        
        # Create a list to store the actual height of each position in the warehouse
        actual_height = [0] * len(warehouse)
        for i in range(len(warehouse)):
            actual_height[i] = max(left_min[i], right_min[i])
        
        # Sort the actual heights of the warehouse in non-decreasing order
        actual_height.sort()
        
        # Two pointers to traverse boxes and actual_height
        box_index = 0
        height_index = 0
        
        # Count the number of boxes that can be placed
        while box_index < len(boxes) and height_index < len(actual_height):
            if boxes[box_index] <= actual_height[height_index]:
                box_index += 1
            height_index += 1
        
        return box_index

def maxBoxesInWarehouse(boxes: List[int], warehouse: List[int]) -> int:
    return Solution().maxBoxesInWarehouse(boxes, warehouse)