import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Convert the number to its binary representation and remove the '0b' prefix
        binary_representation = bin(n)[2:]
        
        # Check if all adjacent bits are different
        for i in range(len(binary_representation) - 1):
            if binary_representation[i] == binary_representation[i + 1]:
                return False
        
        return True

def hasAlternatingBits(n: int) -> bool:
    return Solution().hasAlternatingBits(n)