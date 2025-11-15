import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initial position and direction
        x, y = 0, 0
        idx = 0  # Index to keep track of the current direction
        
        # Process each instruction
        for instruction in instructions:
            if instruction == 'L':
                idx = (idx - 1) % 4  # Turn left
            elif instruction == 'R':
                idx = (idx + 1) % 4  # Turn right
            else:  # instruction == 'G'
                x += directions[idx][0]  # Move in the current direction
                y += directions[idx][1]
        
        # After one cycle of instructions, the robot is bounded
        # if it's back at the origin or not facing north
        return (x == 0 and y == 0) or idx != 0

def isRobotBounded(instructions: str) -> bool:
    return Solution().isRobotBounded(instructions)