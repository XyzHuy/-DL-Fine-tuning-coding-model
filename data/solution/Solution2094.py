import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_numbers = set()
        
        # Generate all possible permutations of length 3
        for perm in permutations(digits, 3):
            # Convert the permutation to an integer
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            # Check if the number has no leading zeros and is even
            if perm[0] != 0 and num % 2 == 0:
                unique_numbers.add(num)
        
        # Return the sorted list of unique numbers
        return sorted(unique_numbers)

def findEvenNumbers(digits: List[int]) -> List[int]:
    return Solution().findEvenNumbers(digits)