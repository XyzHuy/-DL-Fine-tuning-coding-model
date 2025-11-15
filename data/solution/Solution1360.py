import random
import functools
import collections
import string
import math
import datetime


from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Define the date format
        date_format = "%Y-%m-%d"
        
        # Convert the string dates to datetime objects
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)
        
        # Calculate the difference between the two dates
        delta = abs(d2 - d1)
        
        # Return the number of days as an integer
        return delta.days

def daysBetweenDates(date1: str, date2: str) -> int:
    return Solution().daysBetweenDates(date1, date2)