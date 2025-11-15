import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        largest_prime = 0
        n = len(nums)
        
        for i in range(n):
            if is_prime(nums[i][i]):
                largest_prime = max(largest_prime, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                largest_prime = max(largest_prime, nums[i][n - i - 1])
        
        return largest_prime

def diagonalPrime(nums: List[List[int]]) -> int:
    return Solution().diagonalPrime(nums)