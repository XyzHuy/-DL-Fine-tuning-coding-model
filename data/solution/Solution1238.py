import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # Generate the Gray code sequence for 2^n numbers
        gray_code = [i ^ (i >> 1) for i in range(1 << n)]
        
        # Find the index of the start number in the Gray code sequence
        start_index = gray_code.index(start)
        
        # Rotate the sequence so that it starts with the start number
        return gray_code[start_index:] + gray_code[:start_index]

# Example usage:
# sol = Solution()
# print(sol.circularPermutation(2, 3))  # Output: [3, 2, 0, 1]
# print(sol.circularPermutation(3, 2))  # Output: [2, 6, 7, 5, 4, 0, 1, 3]

def circularPermutation(n: int, start: int) -> List[int]:
    return Solution().circularPermutation(n, start)