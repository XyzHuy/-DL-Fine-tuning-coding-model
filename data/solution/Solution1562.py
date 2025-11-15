import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        
        # Initialize the length of groups of 1s
        length = [0] * (n + 2)
        # To keep track of how many groups of a certain length exist
        count = [0] * (n + 1)
        latest_step = -1
        
        for step, pos in enumerate(arr, 1):
            left_length = length[pos - 1]
            right_length = length[pos + 1]
            
            # Decrease the count of the groups that are going to be merged
            count[left_length] -= 1
            count[right_length] -= 1
            
            # Calculate the new length of the group
            new_length = left_length + right_length + 1
            
            # Update the length array
            length[pos] = length[pos - left_length] = length[pos + right_length] = new_length
            
            # Increase the count of the new group length
            count[new_length] += 1
            
            # Check if there is any group of length m
            if count[m] > 0:
                latest_step = step
        
        return latest_step

def findLatestStep(arr: List[int], m: int) -> int:
    return Solution().findLatestStep(arr, m)