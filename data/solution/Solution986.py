import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        intersections = []
        
        while i < len(firstList) and j < len(secondList):
            # Find the intersection between firstList[i] and secondList[j]
            start_max = max(firstList[i][0], secondList[j][0])
            end_min = min(firstList[i][1], secondList[j][1])
            
            # If there is an intersection, add it to the result
            if start_max <= end_min:
                intersections.append([start_max, end_min])
            
            # Move the pointer that has the smaller end
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return intersections

def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    return Solution().intervalIntersection(firstList, secondList)