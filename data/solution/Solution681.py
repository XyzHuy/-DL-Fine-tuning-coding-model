import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nextClosestTime(self, time: str) -> str:
        # Extract the digits from the given time
        digits = set([time[0], time[1], time[3], time[4]])
        
        # Generate all possible valid times using the extracted digits
        def generate_times(digits):
            valid_times = []
            for h1 in digits:
                for h2 in digits:
                    for m1 in digits:
                        for m2 in digits:
                            hour = int(h1 + h2)
                            minute = int(m1 + m2)
                            if hour < 24 and minute < 60:
                                valid_times.append((hour, minute))
            return valid_times
        
        valid_times = generate_times(digits)
        valid_times.sort()  # Sort the valid times
        
        # Convert the current time to minutes since midnight for comparison
        current_hour, current_minute = int(time[:2]), int(time[3:])
        current_total_minutes = current_hour * 60 + current_minute
        
        # Find the next closest time
        for hour, minute in valid_times:
            total_minutes = hour * 60 + minute
            if total_minutes > current_total_minutes:
                return f"{hour:02}:{minute:02}"
        
        # If no time is found, return the earliest possible time
        earliest_hour, earliest_minute = valid_times[0]
        return f"{earliest_hour:02}:{earliest_minute:02}"

def nextClosestTime(time: str) -> str:
    return Solution().nextClosestTime(time)