import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # Convert current and correct times to minutes since midnight
        current_hours, current_minutes = map(int, current.split(':'))
        correct_hours, correct_minutes = map(int, correct.split(':'))
        
        current_total_minutes = current_hours * 60 + current_minutes
        correct_total_minutes = correct_hours * 60 + correct_minutes
        
        # Calculate the difference in minutes
        difference = correct_total_minutes - current_total_minutes
        
        # Define the possible operations in descending order
        operations = [60, 15, 5, 1]
        
        # Count the number of operations needed
        num_operations = 0
        for operation in operations:
            num_operations += difference // operation
            difference %= operation
        
        return num_operations

def convertTime(current: str, correct: str) -> int:
    return Solution().convertTime(current, correct)