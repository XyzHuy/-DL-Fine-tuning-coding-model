import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # The problem can be solved using a probabilistic approach.
        # For n = 1, the probability is 1 because there's only one seat.
        # For n > 1, the probability that the nth person gets their seat is 0.5.
        # This is a known result from the problem's symmetry and recursive nature.
        return 1.0 if n == 1 else 0.5

def nthPersonGetsNthSeat(n: int) -> float:
    return Solution().nthPersonGetsNthSeat(n)