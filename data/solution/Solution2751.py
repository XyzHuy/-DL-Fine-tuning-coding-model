import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Combine positions, healths, and directions into a single list of tuples
        robots = [(pos, health, direction, index) for index, (pos, health, direction) in enumerate(zip(positions, healths, directions))]
        
        # Sort robots by their positions
        robots.sort()
        
        # Stack to keep track of robots moving to the right
        stack = []
        surviving_robots = []
        
        for pos, health, direction, index in robots:
            if direction == 'R':
                # Push the robot moving to the right onto the stack
                stack.append((health, index))
            else:
                # Handle collisions for the robot moving to the left
                while stack and health > 0:
                    top_health, top_index = stack[-1]
                    if health > top_health:
                        stack.pop()
                        health -= 1
                    elif health == top_health:
                        stack.pop()
                        health = 0
                    else:
                        stack[-1] = (top_health - 1, top_index)
                        health = 0
                
                # If the robot moving to the left survived, add it to the surviving robots list
                if health > 0:
                    surviving_robots.append((health, index))
        
        # Add the remaining robots from the stack to the surviving robots list
        surviving_robots.extend(stack)
        
        # Sort the surviving robots by their original index
        surviving_robots.sort(key=lambda x: x[1])
        
        # Extract the healths of the surviving robots
        return [health for health, index in surviving_robots]

def survivedRobotsHealths(positions: List[int], healths: List[int], directions: str) -> List[int]:
    return Solution().survivedRobotsHealths(positions, healths, directions)