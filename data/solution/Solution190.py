import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert the integer to a binary string, remove the '0b' prefix, and pad with zeros to ensure it's 32 bits
        binary_str = format(n, '032b')
        # Reverse the binary string
        reversed_binary_str = binary_str[::-1]
        # Convert the reversed binary string back to an integer
        reversed_int = int(reversed_binary_str, 2)
        return reversed_int

def reverseBits(n: int) -> int:
    return Solution().reverseBits(n)