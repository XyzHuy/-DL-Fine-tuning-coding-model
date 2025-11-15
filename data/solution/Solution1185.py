import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Zeller's Congruence Algorithm to find the day of the week
        if month < 3:
            month += 12
            year -= 1
        
        k = year % 100
        j = year // 100
        
        f = day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j
        day_of_week = f % 7
        
        # Mapping the result to the correct day name
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        return days[day_of_week]

def dayOfTheWeek(day: int, month: int, year: int) -> str:
    return Solution().dayOfTheWeek(day, month, year)