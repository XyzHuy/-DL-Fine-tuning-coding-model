import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Convert target to a max heap by negating the values
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)
        
        total_sum = sum(target)
        
        while True:
            # Get the largest element
            largest = -heapq.heappop(max_heap)
            
            # If the largest element is 1, we can form the target array
            if largest == 1:
                return True
            
            # Calculate the sum of the rest of the elements
            rest_sum = total_sum - largest
            
            # If the rest sum is 0 or the largest element is less than or equal to the rest sum, it's not possible
            if rest_sum == 0 or largest <= rest_sum:
                return False
            
            # Calculate the new value to replace the largest element
            new_value = largest % rest_sum
            
            # If the new value is 0 and the rest sum is not 1, it's not possible
            if new_value == 0 and rest_sum != 1:
                return False
            
            # Update the total sum and push the new value back into the heap
            total_sum = rest_sum + new_value
            heapq.heappush(max_heap, -new_value)

def isPossible(target: List[int]) -> bool:
    return Solution().isPossible(target)