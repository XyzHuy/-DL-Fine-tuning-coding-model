import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29  # February has 29 days in a leap year
        
        return days_in_month[month - 1]

def numberOfDays(year: int, month: int) -> int:
    return Solution().numberOfDays(year, month)