import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisors_sum = 1  # Start with 1 because 1 is a divisor of every number
        sqrt_num = int(num ** 0.5)
        
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        
        return divisors_sum == num

def checkPerfectNumber(num: int) -> bool:
    return Solution().checkPerfectNumber(num)