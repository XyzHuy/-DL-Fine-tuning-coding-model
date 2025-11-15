import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumBoxes(self, n: int) -> int:
        # Function to calculate the number of boxes in the first k triangular layers
        def triangular_layers(k):
            return k * (k + 1) * (k + 2) // 6
        
        # Find the maximum number of complete triangular layers we can form
        k = 0
        while triangular_layers(k + 1) <= n:
            k += 1
        
        # Number of boxes used by complete layers
        used_boxes = triangular_layers(k)
        
        # Number of boxes remaining to be placed
        remaining_boxes = n - used_boxes
        
        # We need to add boxes to the top layer
        additional_boxes = 0
        while remaining_boxes > 0:
            additional_boxes += 1
            remaining_boxes -= additional_boxes
        
        # Total boxes on the floor is the number of boxes in the k-th triangular layer plus any additional boxes on the top layer
        return triangular_layers(k) - triangular_layers(k - 1) + additional_boxes

# Example usage:
# sol = Solution()
# print(sol.minimumBoxes(3))  # Output: 3
# print(sol.minimumBoxes(4))  # Output: 3
# print(sol.minimumBoxes(10)) # Output: 6

def minimumBoxes(n: int) -> int:
    return Solution().minimumBoxes(n)