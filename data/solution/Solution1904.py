import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def convert_to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        login_minutes = convert_to_minutes(loginTime)
        logout_minutes = convert_to_minutes(logoutTime)
        
        # If logout time is on the next day
        if logout_minutes < login_minutes:
            logout_minutes += 24 * 60
        
        # Round up the login time to the next 15-minute mark
        if login_minutes % 15 != 0:
            login_minutes += (15 - login_minutes % 15)
        
        # Round down the logout time to the previous 15-minute mark
        logout_minutes -= logout_minutes % 15
        
        # Calculate the number of full 15-minute intervals
        return max(0, (logout_minutes - login_minutes) // 15)

def numberOfRounds(loginTime: str, logoutTime: str) -> int:
    return Solution().numberOfRounds(loginTime, logoutTime)