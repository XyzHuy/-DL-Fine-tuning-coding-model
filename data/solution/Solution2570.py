import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Create a dictionary to store the sum of values for each id
        id_value_map = {}
        
        # Add values from nums1 to the dictionary
        for id, value in nums1:
            if id in id_value_map:
                id_value_map[id] += value
            else:
                id_value_map[id] = value
        
        # Add values from nums2 to the dictionary
        for id, value in nums2:
            if id in id_value_map:
                id_value_map[id] += value
            else:
                id_value_map[id] = value
        
        # Convert the dictionary to a sorted list of [id, value] pairs
        result = sorted(id_value_map.items(), key=lambda x: x[0])
        
        return result

def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    return Solution().mergeArrays(nums1, nums2)