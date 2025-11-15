import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Count the frequency of each number in the array
        frequency = Counter(arr)
        
        # Initialize the variable to store the largest lucky integer
        largest_lucky = -1
        
        # Iterate through the frequency dictionary
        for num, freq in frequency.items():
            # Check if the number is a lucky integer
            if num == freq:
                # Update the largest lucky integer
                largest_lucky = max(largest_lucky, num)
        
        return largest_lucky

def findLucky(arr: List[int]) -> int:
    return Solution().findLucky(arr)