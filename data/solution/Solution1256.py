import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def encode(self, num: int) -> str:
        # Convert num + 1 to binary and remove the '0b' prefix
        binary_representation = bin(num + 1)[2:]
        # Remove the leading '1'
        encoded_string = binary_representation[1:]
        return encoded_string

def encode(num: int) -> str:
    return Solution().encode(num)