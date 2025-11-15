import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine the names and heights into a list of tuples
        people = list(zip(heights, names))
        # Sort the list of tuples by height in descending order
        people.sort(reverse=True)
        # Extract the sorted names
        sorted_names = [name for height, name in people]
        return sorted_names

def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    return Solution().sortPeople(names, heights)