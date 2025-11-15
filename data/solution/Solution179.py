import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings for comparison
        nums_str = list(map(str, nums))
        
        # Sort the numbers based on custom comparator
        # We compare two numbers x and y by comparing xy and yx
        # If xy > yx, x should come before y
        nums_str.sort(key=lambda x: x*10, reverse=True)
        
        # Join the sorted numbers into a single string
        largest_number = ''.join(nums_str)
        
        # Handle the case where the result is all zeros
        return '0' if largest_number[0] == '0' else largest_number

def largestNumber(nums: List[int]) -> str:
    return Solution().largestNumber(nums)