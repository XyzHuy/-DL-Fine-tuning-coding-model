import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # Since primeOne and primeTwo are distinct primes, they are coprime.
        # We can use the formula for the Frobenius number for two coprime integers.
        return primeOne * primeTwo - primeOne - primeTwo

def mostExpensiveItem(primeOne: int, primeTwo: int) -> int:
    return Solution().mostExpensiveItem(primeOne, primeTwo)