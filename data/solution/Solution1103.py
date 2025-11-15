import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Initialize the result array with zeros
        result = [0] * num_people
        i = 0  # This will keep track of the current number of candies to give
        
        # While we have enough candies to give the next person their due amount
        while candies > 0:
            # Calculate the number of candies to give to the current person
            to_give = min(i + 1, candies)
            # Add the candies to the current person's total
            result[i % num_people] += to_give
            # Subtract the given candies from the total
            candies -= to_give
            # Move to the next person
            i += 1
        
        return result

def distributeCandies(candies: int, num_people: int) -> List[int]:
    return Solution().distributeCandies(candies, num_people)