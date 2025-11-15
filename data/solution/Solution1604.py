import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def convert_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        # Dictionary to store the access times for each person
        access_times = defaultdict(list)
        
        # Populate the dictionary with the access times
        for name, time in zip(keyName, keyTime):
            access_times[name].append(convert_to_minutes(time))
        
        # List to store the names of people who triggered the alert
        alerted_names = []
        
        # Check each person's access times
        for name, times in access_times.items():
            # Sort the access times
            times.sort()
            # Check for any three access times within one hour
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    alerted_names.append(name)
                    break
        
        # Return the sorted list of names
        return sorted(alerted_names)

def alertNames(keyName: List[str], keyTime: List[str]) -> List[str]:
    return Solution().alertNames(keyName, keyTime)