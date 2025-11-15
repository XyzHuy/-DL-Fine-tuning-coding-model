import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Create a dictionary to store the change in the number of flowers at each point in time
        timeline = defaultdict(int)
        
        # For each flower, increment the count at its start time and decrement at the time just after its end time
        for start, end in flowers:
            timeline[start] += 1
            timeline[end + 1] -= 1
        
        # Sort the timeline keys (unique times) to process in chronological order
        times = sorted(timeline.keys())
        
        # Initialize the number of flowers and the prefix sum array
        num_flowers = 0
        prefix_sum = []
        
        # Compute the prefix sum array which will store the number of flowers at each unique time
        for time in times:
            num_flowers += timeline[time]
            prefix_sum.append((time, num_flowers))
        
        # Create a dictionary from the prefix sum array for O(1) lookups
        prefix_sum_dict = dict(prefix_sum)
        
        # Binary search function to find the number of flowers at a given time
        def get_num_flowers(arr, target):
            low, high = 0, len(arr) - 1
            while low < high:
                mid = (low + high + 1) // 2
                if arr[mid][0] <= target:
                    low = mid
                else:
                    high = mid - 1
            return prefix_sum_dict[arr[low][0]]
        
        # For each person, find the number of flowers in bloom at their arrival time
        result = []
        for person in people:
            if person < times[0]:
                result.append(0)
            elif person > times[-1]:
                result.append(0)
            else:
                result.append(get_num_flowers(prefix_sum, person))
        
        return result

def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
    return Solution().fullBloomFlowers(flowers, people)