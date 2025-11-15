import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        # Helper function to determine if a year is a leap year
        def is_leap_year(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Parse the input date
        year, month, day = map(int, date.split('-'))
        
        # If it's a leap year, February has 29 days
        if is_leap_year(year):
            days_in_month[1] = 29
        
        # Calculate the day number of the year
        day_of_year = sum(days_in_month[:month - 1]) + day
        
        return day_of_year

def dayOfYear(date: str) -> int:
    return Solution().dayOfYear(date)