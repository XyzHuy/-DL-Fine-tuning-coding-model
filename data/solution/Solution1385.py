import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_value = 0
        
        for num1 in arr1:
            if all(abs(num1 - num2) > d for num2 in arr2):
                distance_value += 1
                
        return distance_value

def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    return Solution().findTheDistanceValue(arr1, arr2, d)