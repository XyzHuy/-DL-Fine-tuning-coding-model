import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_ones = sum(arr)
        
        # If there are no ones, we can split into any three parts
        if total_ones == 0:
            return [0, len(arr) - 1]
        
        # If the total number of ones is not divisible by 3, we cannot split into three equal parts
        if total_ones % 3 != 0:
            return [-1, -1]
        
        # Number of ones in each part
        ones_per_part = total_ones // 3
        
        # Find the starting index of the first, second, and third parts
        first_part_start = second_part_start = third_part_start = 0
        ones_count = 0
        
        for i, num in enumerate(arr):
            if num == 1:
                ones_count += 1
                if ones_count == 1:
                    first_part_start = i
                elif ones_count == ones_per_part + 1:
                    second_part_start = i
                elif ones_count == 2 * ones_per_part + 1:
                    third_part_start = i
                    break
        
        # Calculate the length of the binary representation of the third part
        length_of_part = len(arr) - third_part_start
        
        # Check if the three parts are equal
        if (first_part_start + length_of_part <= second_part_start and
            second_part_start + length_of_part <= third_part_start and
            arr[first_part_start:first_part_start + length_of_part] == arr[second_part_start:second_part_start + length_of_part] == arr[third_part_start:]):
            return [first_part_start + length_of_part - 1, second_part_start + length_of_part]
        
        return [-1, -1]

def threeEqualParts(arr: List[int]) -> List[int]:
    return Solution().threeEqualParts(arr)