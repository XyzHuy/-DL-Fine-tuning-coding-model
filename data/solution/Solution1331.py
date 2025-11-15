import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Create a sorted list of unique elements
        sorted_unique_arr = sorted(set(arr))
        
        # Create a dictionary to map each element to its rank
        rank_dict = {value: idx + 1 for idx, value in enumerate(sorted_unique_arr)}
        
        # Replace each element in the original array with its rank
        return [rank_dict[value] for value in arr]

def arrayRankTransform(arr: List[int]) -> List[int]:
    return Solution().arrayRankTransform(arr)