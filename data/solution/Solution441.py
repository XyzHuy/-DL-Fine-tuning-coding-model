import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Using the formula derived from the sum of the first k natural numbers: k(k + 1)/2 <= n
        # Rearranging gives us a quadratic equation: k^2 + k - 2n <= 0
        # Solving for k using the quadratic formula: k = (-b + sqrt(b^2 - 4ac)) / 2a
        # Here, a = 1, b = 1, c = -2n
        import math
        k = (-1 + math.sqrt(1 + 8 * n)) / 2
        return int(k)

def arrangeCoins(n: int) -> int:
    return Solution().arrangeCoins(n)