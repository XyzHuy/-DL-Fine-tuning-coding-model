import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Count the number of people for each age
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        requests = 0
        
        # Iterate over each age x
        for age_x in range(15, 121):  # No one under 15 can send friend requests
            count_x = count[age_x]
            # Iterate over each age y
            for age_y in range(15, 121):
                count_y = count[age_y]
                # Check the conditions for sending a friend request
                if 0.5 * age_x + 7 < age_y <= age_x:
                    requests += count_x * count_y
                    if age_x == age_y:
                        requests -= count_x  # Subtract self-requests
        
        return requests

def numFriendRequests(ages: List[int]) -> int:
    return Solution().numFriendRequests(ages)