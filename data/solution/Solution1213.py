import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Convert the lists to sets to find the intersection
        set1 = set(arr1)
        set2 = set(arr2)
        set3 = set(arr3)
        
        # Find the intersection of the three sets
        intersection_set = set1.intersection(set2, set3)
        
        # Convert the set back to a sorted list
        result = sorted(intersection_set)
        
        return result

def arraysIntersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    return Solution().arraysIntersection(arr1, arr2, arr3)