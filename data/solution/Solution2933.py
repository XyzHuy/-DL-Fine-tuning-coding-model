import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # Dictionary to store access times for each employee
        employee_access = defaultdict(list)
        
        # Populate the dictionary with access times
        for name, time in access_times:
            # Convert time to minutes for easier comparison
            time_in_minutes = int(time[:2]) * 60 + int(time[2:])
            employee_access[name].append(time_in_minutes)
        
        # List to store names of high-access employees
        high_access_employees = []
        
        # Check each employee's access times
        for name, times in employee_access.items():
            # Sort the access times
            times.sort()
            # Check for any three access times within one hour
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    high_access_employees.append(name)
                    break
        
        return high_access_employees

def findHighAccessEmployees(access_times: List[List[str]]) -> List[str]:
    return Solution().findHighAccessEmployees(access_times)