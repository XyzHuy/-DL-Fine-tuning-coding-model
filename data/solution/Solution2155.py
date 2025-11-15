import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # Initialize the count of 0's in numsleft and 1's in numsright
        zeros_left = 0
        ones_right = sum(nums)
        
        # Initialize the maximum score and the result list
        max_score = ones_right
        result = [0]
        
        # Iterate through each possible index to divide the array
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_left += 1
            else:
                ones_right -= 1
            
            # Calculate the current division score
            current_score = zeros_left + ones_right
            
            # Update the result if a new maximum score is found
            if current_score > max_score:
                max_score = current_score
                result = [i + 1]
            elif current_score == max_score:
                result.append(i + 1)
        
        return result

def maxScoreIndices(nums: List[int]) -> List[int]:
    return Solution().maxScoreIndices(nums)