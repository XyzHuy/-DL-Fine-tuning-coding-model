import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Count the number of zeros in the binary string
        zero_count = binary.count('0')
        
        # If there are no zeros or only one zero, the string is already maximum
        if zero_count <= 1:
            return binary
        
        # Find the index of the first zero
        first_zero_index = binary.index('0')
        
        # The result will have all ones except for one zero
        # The zero will be at the position: first_zero_index + zero_count - 1
        # All other positions will be ones
        return '1' * (first_zero_index + zero_count - 1) + '0' + '1' * (len(binary) - first_zero_index - zero_count)

def maximumBinaryString(binary: str) -> str:
    return Solution().maximumBinaryString(binary)