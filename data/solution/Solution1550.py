import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Iterate through the array with a window of size 3
        for i in range(len(arr) - 2):
            # Check if the current element, the next element, and the one after that are all odd
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False

def threeConsecutiveOdds(arr: List[int]) -> bool:
    return Solution().threeConsecutiveOdds(arr)