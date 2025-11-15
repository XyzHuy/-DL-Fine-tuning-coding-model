import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
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
        
        prime_set_bits_count = 0
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if is_prime(set_bits):
                prime_set_bits_count += 1
        
        return prime_set_bits_count

def countPrimeSetBits(left: int, right: int) -> int:
    return Solution().countPrimeSetBits(left, right)