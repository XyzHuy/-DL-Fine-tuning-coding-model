import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events for each start and end of buildings
        events = []
        for start, end, height in buildings:
            events.append((start, height, 1))  # start of a building
            events.append((end, height, -1))   # end of a building
        
        # Sort events: first by position, then by type (start before end)
        events.sort()
        
        # Initialize variables to track the current state
        current_position = 0
        total_height = 0
        count_buildings = 0
        result = []
        
        for position, height, event_type in events:
            # If there is a change in position, finalize the previous segment
            if position != current_position:
                if count_buildings > 0:
                    average_height = total_height // count_buildings
                    # If the result is not empty and the last segment can be merged
                    if result and result[-1][1] == current_position and result[-1][2] == average_height:
                        result[-1][1] = position  # Extend the last segment
                    else:
                        result.append([current_position, position, average_height])
                current_position = position
            
            # Update the total height and count of buildings
            if event_type == 1:  # start of a building
                total_height += height
                count_buildings += 1
            else:  # end of a building
                total_height -= height
                count_buildings -= 1
        
        return result

def averageHeightOfBuildings(buildings: List[List[int]]) -> List[List[int]]:
    return Solution().averageHeightOfBuildings(buildings)