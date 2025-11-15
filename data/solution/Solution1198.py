import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # Initialize the set with the first row's elements
        common_elements = set(mat[0])
        
        # Iterate over the remaining rows
        for row in mat[1:]:
            # Update the set to keep only the common elements
            common_elements.intersection_update(row)
            
            # If at any point the set is empty, return -1
            if not common_elements:
                return -1
        
        # Return the smallest common element
        return min(common_elements) if common_elements else -1

def smallestCommonElement(mat: List[List[int]]) -> int:
    return Solution().smallestCommonElement(mat)