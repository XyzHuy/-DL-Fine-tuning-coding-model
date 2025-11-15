import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor_arr1 = 0
        xor_arr2 = 0
        
        # Compute XOR of all elements in arr1
        for num in arr1:
            xor_arr1 ^= num
        
        # Compute XOR of all elements in arr2
        for num in arr2:
            xor_arr2 ^= num
        
        # Return the AND of the two XOR results
        return xor_arr1 & xor_arr2

def getXORSum(arr1: List[int], arr2: List[int]) -> int:
    return Solution().getXORSum(arr1, arr2)