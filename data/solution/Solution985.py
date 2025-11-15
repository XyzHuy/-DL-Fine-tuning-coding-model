import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Calculate the initial sum of even numbers
        even_sum = sum(num for num in nums if num % 2 == 0)
        answer = []
        
        for val, index in queries:
            # If the current number at index is even, subtract it from even_sum
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            # Apply the query
            nums[index] += val
            
            # If the new number at index is even, add it to even_sum
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            # Append the current even_sum to the answer list
            answer.append(even_sum)
        
        return answer

def sumEvenAfterQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().sumEvenAfterQueries(nums, queries)