import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findComplement(self, num: int) -> int:
        # Convert the number to its binary representation without the '0b' prefix
        binary_representation = bin(num)[2:]
        
        # Create a mask with the same length as the binary representation, filled with 1s
        mask = int('1' * len(binary_representation), 2)
        
        # XOR the number with the mask to get the complement
        complement = num ^ mask
        
        return complement

def findComplement(num: int) -> int:
    return Solution().findComplement(num)