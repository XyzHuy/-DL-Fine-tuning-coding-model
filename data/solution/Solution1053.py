import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # Traverse the array from the end to find the first element that is greater than the element next to it
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        
        # If no such element is found, the array is the smallest permutation
        if i == -1:
            return arr
        
        # Find the largest element smaller than arr[i] to the right of arr[i]
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        
        # To ensure the lexicographically largest permutation, find the rightmost element that is equal to arr[j]
        while j > 0 and arr[j] == arr[j - 1]:
            j -= 1
        
        # Swap the elements at indices i and j
        arr[i], arr[j] = arr[j], arr[i]
        
        return arr

def prevPermOpt1(arr: List[int]) -> List[int]:
    return Solution().prevPermOpt1(arr)