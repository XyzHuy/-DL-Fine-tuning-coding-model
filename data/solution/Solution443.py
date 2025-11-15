import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        write_index = 0
        read_index = 0
        
        while read_index < len(chars):
            char = chars[read_index]
            count = 0
            
            # Count the number of occurrences of the current character
            while read_index < len(chars) and chars[read_index] == char:
                read_index += 1
                count += 1
            
            # Write the character to the write_index
            chars[write_index] = char
            write_index += 1
            
            # If the count is greater than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        
        return write_index

def compress(chars: List[str]) -> int:
    return Solution().compress(chars)