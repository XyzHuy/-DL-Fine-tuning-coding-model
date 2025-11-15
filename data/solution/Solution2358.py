import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        k = 0
        while (k * (k + 1)) // 2 <= n:
            k += 1
        return k - 1

# Example usage:
# solution = Solution()
# print(solution.maximumGroups([10, 6, 12, 7, 3, 5]))  # Output: 3
# print(solution.maximumGroups([8, 8]))  # Output: 1

def maximumGroups(grades: List[int]) -> int:
    return Solution().maximumGroups(grades)