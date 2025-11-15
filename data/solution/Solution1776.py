import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        result = [-1.0] * n
        stack = []  # This stack will store indices of cars

        # We iterate from the last car to the first car
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            
            # Maintain the stack such that we always have cars that can be collided with
            while stack:
                top = stack[-1]
                top_pos, top_speed = cars[top]
                
                # If the current car is faster or has the same speed as the top car in the stack, it cannot collide with it
                if speed <= top_speed:
                    stack.pop()
                    continue
                
                # Calculate the collision time
                collision_time = (top_pos - pos) / (speed - top_speed)
                
                # If the top car will collide with another car after this collision time, we need to check if this collision is valid
                if result[top] != -1 and collision_time >= result[top]:
                    stack.pop()
                    continue
                
                # Valid collision time found
                result[i] = collision_time
                break
            
            # Push the current car index onto the stack
            stack.append(i)
        
        return result

def getCollisionTimes(cars: List[List[int]]) -> List[float]:
    return Solution().getCollisionTimes(cars)