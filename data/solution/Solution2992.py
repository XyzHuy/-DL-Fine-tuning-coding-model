import random
import functools
import collections
import string
import math
import datetime


from math import gcd

class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        def backtrack(pos, used):
            if pos > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                if not used[num] and gcd(num, pos) == 1:
                    used[num] = True
                    count += backtrack(pos + 1, used)
                    used[num] = False
            
            return count
        
        used = [False] * (n + 1)
        return backtrack(1, used)

# Example usage:
# sol = Solution()
# print(sol.selfDivisiblePermutationCount(1))  # Output: 1
# print(sol.selfDivisiblePermutationCount(2))  # Output: 1
# print(sol.selfDivisiblePermutationCount(3))  # Output: 3

def selfDivisiblePermutationCount(n: int) -> int:
    return Solution().selfDivisiblePermutationCount(n)