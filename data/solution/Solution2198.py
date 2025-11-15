import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_nums = list(count.keys())
        n = len(unique_nums)
        result = 0
        
        # Iterate over all possible triplets (i, j, k)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    a, b, c = unique_nums[i], unique_nums[j], unique_nums[k]
                    total = a + b + c
                    
                    # Check divisibility conditions
                    divisors = sum(total % x == 0 for x in [a, b, c])
                    
                    if divisors == 1:
                        # Count permutations based on the number of unique elements
                        if i == j == k:
                            result += count[a] * (count[a] - 1) * (count[a] - 2) // 6
                        elif i == j:
                            result += count[a] * (count[a] - 1) // 2 * count[c]
                        elif j == k:
                            result += count[a] * count[b] * (count[b] - 1) // 2
                        elif i == k:
                            result += count[a] * (count[a] - 1) // 2 * count[b]
                        else:
                            result += count[a] * count[b] * count[c]
        
        return result * 6

# Example usage:
# sol = Solution()
# print(sol.singleDivisorTriplet([4, 6, 7, 3, 2]))  # Output: 12
# print(sol.singleDivisorTriplet([1, 2, 2]))        # Output: 6
# print(sol.singleDivisorTriplet([1, 1, 1]))        # Output: 0

def singleDivisorTriplet(nums: List[int]) -> int:
    return Solution().singleDivisorTriplet(nums)