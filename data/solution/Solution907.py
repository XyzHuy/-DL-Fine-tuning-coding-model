import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        left = [0] * n
        right = [0] * n

        # Calculate the number of subarrays for which each element is the minimum
        # from the left side
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i - stack[-1] - 1 if stack else i
            stack.append(i)

        stack = []

        # Calculate the number of subarrays for which each element is the minimum
        # from the right side
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i - 1 if stack else n - i - 1
            stack.append(i)

        # Calculate the result
        result = 0
        for i in range(n):
            result = (result + arr[i] * (left[i] + 1) * (right[i] + 1)) % MOD

        return result

def sumSubarrayMins(arr: List[int]) -> int:
    return Solution().sumSubarrayMins(arr)