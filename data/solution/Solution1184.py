import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        clockwise_distance = sum(distance[start:destination])
        counterclockwise_distance = sum(distance) - clockwise_distance
        
        return min(clockwise_distance, counterclockwise_distance)

def distanceBetweenBusStops(distance: List[int], start: int, destination: int) -> int:
    return Solution().distanceBetweenBusStops(distance, start, destination)