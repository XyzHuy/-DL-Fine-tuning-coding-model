import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Dictionary to store the two largest numbers for each largest digit
        max_pairs = {}
        
        for num in nums:
            # Find the largest digit in the number
            largest_digit = max(str(num))
            
            # If the largest digit is not in the dictionary, add it with the current number
            if largest_digit not in max_pairs:
                max_pairs[largest_digit] = [num]
            else:
                # Get the list of numbers for this largest digit
                pair = max_pairs[largest_digit]
                
                # If we have less than two numbers, add the current number
                if len(pair) < 2:
                    pair.append(num)
                else:
                    # If we have two numbers, replace the smaller one if the current number is larger
                    if num > pair[0]:
                        if pair[0] < pair[1]:
                            pair[0] = num
                        else:
                            pair[1] = num
                    elif num > pair[1]:
                        pair[1] = num
                
                # Update the dictionary
                max_pairs[largest_digit] = pair
        
        # Calculate the maximum sum of pairs
        max_sum = -1
        for pair in max_pairs.values():
            if len(pair) == 2:
                max_sum = max(max_sum, sum(pair))
        
        return max_sum

def maxSum(nums: List[int]) -> int:
    return Solution().maxSum(nums)