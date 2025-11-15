import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Define a key function for sorting
        def sort_key(x):
            # Count the number of 1's in the binary representation of x
            ones_count = bin(x).count('1')
            # Return a tuple (number of 1's, the number itself)
            return (ones_count, x)
        
        # Sort the array using the custom key function
        return sorted(arr, key=sort_key)

def sortByBits(arr: List[int]) -> List[int]:
    return Solution().sortByBits(arr)