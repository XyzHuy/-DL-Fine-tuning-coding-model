import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        # Create a list to store the indices of occurrences of x in nums
        occurrences = []
        
        # Iterate over nums to find all occurrences of x
        for index, num in enumerate(nums):
            if num == x:
                occurrences.append(index)
        
        # Prepare the answer list based on the queries
        answer = []
        for query in queries:
            # If there are at least query occurrences of x, append the index of the query-th occurrence
            if query <= len(occurrences):
                answer.append(occurrences[query - 1])
            else:
                # Otherwise, append -1
                answer.append(-1)
        
        return answer

def occurrencesOfElement(nums: List[int], queries: List[int], x: int) -> List[int]:
    return Solution().occurrencesOfElement(nums, queries, x)