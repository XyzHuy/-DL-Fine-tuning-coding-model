import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Generate all possible sequential digit numbers
        sequential_numbers = []
        for start in range(1, 9):
            number = 0
            for i in range(start, 10):
                number = number * 10 + i
                if 10 <= number <= high:
                    sequential_numbers.append(number)
        
        # Filter the numbers that are within the range [low, high]
        result = [num for num in sequential_numbers if low <= num <= high]
        
        # Return the sorted list (though it should already be sorted)
        return sorted(result)

# Example usage:
# sol = Solution()
# print(sol.sequentialDigits(100, 300))  # Output: [123, 234]
# print(sol.sequentialDigits(1000, 13000))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]

def sequentialDigits(low: int, high: int) -> List[int]:
    return Solution().sequentialDigits(low, high)