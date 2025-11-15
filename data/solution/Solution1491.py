import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        # Remove the minimum and maximum salary from the list
        salary.remove(min(salary))
        salary.remove(max(salary))
        
        # Calculate the average of the remaining salaries
        return sum(salary) / len(salary)

def average(salary: List[int]) -> float:
    return Solution().average(salary)