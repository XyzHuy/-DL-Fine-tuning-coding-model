import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # Sort the list of people by their weights
        left, right = 0, len(people) - 1  # Initialize two pointers
        boats = 0  # Initialize the count of boats
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Move the left pointer to the right if the lightest and heaviest person can share a boat
            right -= 1  # Always move the right pointer to the left after each iteration
            boats += 1  # Increment the boat count
        
        return boats  # Return the total number of boats needed

def numRescueBoats(people: List[int], limit: int) -> int:
    return Solution().numRescueBoats(people, limit)