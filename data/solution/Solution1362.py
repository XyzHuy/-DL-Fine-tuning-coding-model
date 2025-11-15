import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_closest_divisors(n):
            # Start checking from the square root of n and go downwards
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]
        
        # Find closest divisors for num + 1 and num + 2
        divisors1 = find_closest_divisors(num + 1)
        divisors2 = find_closest_divisors(num + 2)
        
        # Compare the absolute differences and return the closest pair
        if abs(divisors1[0] - divisors1[1]) < abs(divisors2[0] - divisors2[1]):
            return divisors1
        else:
            return divisors2

def closestDivisors(num: int) -> List[int]:
    return Solution().closestDivisors(num)