import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def divisorGame(self, n: int) -> bool:
        # Alice wins if and only if n is even.
        # This is because if n is even, Alice can always choose x = 1, making n odd for Bob.
        # If n is odd, any divisor x will make n - x even, giving Alice an even number on her next turn.
        # Eventually, this strategy will lead to Bob being faced with n = 1, and he will lose.
        return n % 2 == 0

def divisorGame(n: int) -> bool:
    return Solution().divisorGame(n)