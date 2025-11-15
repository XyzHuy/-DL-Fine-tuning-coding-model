import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        # Initialize the answer list with zeros
        answer = [0] * len(nums)
        
        # Convert each number to its binary representation with leading zeros
        binary_nums = [format(num, f'0{m}b') for num in nums]
        
        # Iterate over each number in the list
        for i in range(len(nums)):
            max_distance = 0
            # Compare the current number with every other number
            for j in range(len(nums)):
                if i == j:
                    continue
                # Calculate the Hamming distance
                distance = sum(b1 != b2 for b1, b2 in zip(binary_nums[i], binary_nums[j]))
                # Update the maximum distance found
                max_distance = max(max_distance, distance)
            # Store the maximum distance in the answer list
            answer[i] = max_distance
        
        return answer

def maxHammingDistances(nums: List[int], m: int) -> List[int]:
    return Solution().maxHammingDistances(nums, m)