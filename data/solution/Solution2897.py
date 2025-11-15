import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 32  # To count the number of times each bit is set across all numbers
        
        # Count the bits
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit_count[i] += 1
        
        # Construct the k largest numbers
        selected_numbers = [0] * k
        for _ in range(k):
            current_number = 0
            for i in range(32):
                if bit_count[i] > 0:
                    current_number |= (1 << i)
                    bit_count[i] -= 1
            selected_numbers.append(current_number)
        
        # Calculate the sum of squares of the selected numbers
        result = sum(x * x for x in selected_numbers) % MOD
        return result

# Example usage:
# sol = Solution()
# print(sol.maxSum([2, 6, 5, 8], 2))  # Output: 261
# print(sol.maxSum([4, 5, 4, 7], 3))  # Output: 90

def maxSum(nums: List[int], k: int) -> int:
    return Solution().maxSum(nums, k)