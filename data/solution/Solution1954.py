import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        k = 0
        total_apples = 0
        
        while total_apples < neededApples:
            k += 1
            # Number of apples in the k-th layer
            apples_in_layer = 12 * k * k
            total_apples += apples_in_layer
        
        # The side length of the square plot is 2k
        side_length = 2 * k
        # The perimeter is 4 * side_length
        perimeter = 4 * side_length
        
        return perimeter

# Example usage:
# sol = Solution()
# print(sol.minimumPerimeter(1))  # Output: 8
# print(sol.minimumPerimeter(13)) # Output: 16
# print(sol.minimumPerimeter(1000000000)) # Output: 5040

def minimumPerimeter(neededApples: int) -> int:
    return Solution().minimumPerimeter(neededApples)