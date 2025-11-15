import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # Sort the boxes in ascending order
        boxes.sort()
        
        # Modify the warehouse list to reflect the minimum height encountered so far from the left
        min_height = float('inf')
        for i in range(len(warehouse)):
            min_height = min(min_height, warehouse[i])
            warehouse[i] = min_height
        
        # Use two pointers to try to fit the smallest box into the smallest available room
        box_index = 0
        room_index = len(warehouse) - 1
        
        while box_index < len(boxes) and room_index >= 0:
            if boxes[box_index] <= warehouse[room_index]:
                box_index += 1  # Successfully placed a box
            room_index -= 1  # Move to the next room from the right
        
        return box_index

def maxBoxesInWarehouse(boxes: List[int], warehouse: List[int]) -> int:
    return Solution().maxBoxesInWarehouse(boxes, warehouse)