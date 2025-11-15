import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # Helper function to count the number of leading 1s in the byte
        def count_leading_ones(byte):
            mask = 0b10000000
            count = 0
            while mask & byte:
                count += 1
                mask >>= 1
            return count
        
        i = 0
        while i < len(data):
            leading_ones = count_leading_ones(data[i])
            
            # Determine the number of bytes for the current character
            if leading_ones == 0:
                # 1-byte character
                i += 1
            elif 2 <= leading_ones <= 4:
                # n-byte character
                num_bytes = leading_ones
                # Check if there are enough bytes in the data
                if i + num_bytes > len(data):
                    return False
                # Check the following num_bytes - 1 bytes
                for j in range(i + 1, i + num_bytes):
                    if (data[j] & 0b11000000) != 0b10000000:
                        return False
                i += num_bytes
            else:
                # Invalid starting byte
                return False
        
        return True

def validUtf8(data: List[int]) -> bool:
    return Solution().validUtf8(data)