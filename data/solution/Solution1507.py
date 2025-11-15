import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reformatDate(self, date: str) -> str:
        # Create a dictionary to map month abbreviations to their respective two-digit numbers
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        
        # Split the input date string into day, month, and year
        day, month, year = date.split()
        
        # Extract the numeric part of the day and pad it with a leading zero if necessary
        day_number = day[:-2].zfill(2)
        
        # Get the two-digit month number from the month_map
        month_number = month_map[month]
        
        # Return the reformatted date string in the format YYYY-MM-DD
        return f"{year}-{month_number}-{day_number}"

def reformatDate(date: str) -> str:
    return Solution().reformatDate(date)