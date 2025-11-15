import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # Dictionary to store unique active minutes for each user
        user_active_minutes = defaultdict(set)
        
        # Populate the dictionary with user actions
        for user_id, time in logs:
            user_active_minutes[user_id].add(time)
        
        # Initialize the result array with zeros
        result = [0] * k
        
        # Count the number of users for each UAM value
        for active_minutes in user_active_minutes.values():
            uam = len(active_minutes)
            if uam <= k:
                result[uam - 1] += 1
        
        return result

def findingUsersActiveMinutes(logs: List[List[int]], k: int) -> List[int]:
    return Solution().findingUsersActiveMinutes(logs, k)