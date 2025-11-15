import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Calculate the number of satisfied customers without using the secret technique
        base_satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        
        # Calculate the additional satisfied customers if the secret technique is used for the first 'minutes' window
        max_additional = 0
        current_additional = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 1:
                current_additional += customers[i]
            
            # Slide the window
            if i >= minutes and grumpy[i - minutes] == 1:
                current_additional -= customers[i - minutes]
            
            # Update the maximum additional satisfied customers
            max_additional = max(max_additional, current_additional)
        
        # The result is the base satisfied customers plus the maximum additional satisfied customers
        return base_satisfied + max_additional

def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    return Solution().maxSatisfied(customers, grumpy, minutes)