import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        # Initialize penalties for closing at hour 0
        penalty = customers.count('Y')
        min_penalty = penalty
        best_hour = 0
        
        # Iterate over each hour to calculate penalty if closing at that hour
        for j in range(1, n + 1):
            if customers[j - 1] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            # Update minimum penalty and best closing hour
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j
        
        return best_hour

def bestClosingTime(customers: str) -> int:
    return Solution().bestClosingTime(customers)