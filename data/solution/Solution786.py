import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def count_and_find_mid(mid):
            count = 0
            j = 1
            numerator = 0
            denominator = 1
            for i in range(len(arr)):
                while j < len(arr) and arr[i] / arr[j] > mid:
                    j += 1
                if j == len(arr):
                    break
                count += (len(arr) - j)
                if arr[i] / arr[j] > numerator / denominator:
                    numerator, denominator = arr[i], arr[j]
            return count, numerator, denominator

        left, right = 0.0, 1.0
        while right - left > 1e-8:
            mid = (left + right) / 2
            count, numerator, denominator = count_and_find_mid(mid)
            if count == k:
                return [numerator, denominator]
            elif count < k:
                left = mid
            else:
                right = mid
        return []

# Example usage:
# sol = Solution()
# print(sol.kthSmallestPrimeFraction([1, 2, 3, 5], 3))  # Output: [2, 5]
# print(sol.kthSmallestPrimeFraction([1, 7], 1))        # Output: [1, 7]

def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    return Solution().kthSmallestPrimeFraction(arr, k)