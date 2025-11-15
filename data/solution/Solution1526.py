import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # The minimum number of operations is the sum of the differences
        # between consecutive elements where the next element is greater than the current.
        # We also need to add the first element of the target array to the result
        # because that represents the initial increment to get to the first element.
        operations = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        return operations

def minNumberOperations(target: List[int]) -> int:
    return Solution().minNumberOperations(target)