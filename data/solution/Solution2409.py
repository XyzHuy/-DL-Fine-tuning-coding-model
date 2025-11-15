import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Number of days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert MM-DD to the day of the year
        def to_day_of_year(date: str) -> int:
            month, day = map(int, date.split('-'))
            # Days before the current month
            days = sum(days_in_month[:month - 1])
            # Days in the current month
            days += day
            return days
        
        # Convert all dates to day of the year
        arriveAlice = to_day_of_year(arriveAlice)
        leaveAlice = to_day_of_year(leaveAlice)
        arriveBob = to_day_of_year(arriveBob)
        leaveBob = to_day_of_year(leaveBob)
        
        # Calculate the overlap
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        
        # If start is after end, there is no overlap
        if start > end:
            return 0
        
        # Return the number of overlapping days
        return end - start + 1

def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    return Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)