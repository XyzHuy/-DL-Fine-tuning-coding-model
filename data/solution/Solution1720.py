import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # Initialize the result array with the first element
        arr = [first]
        
        # Iterate through the encoded array
        for num in encoded:
            # Decode the next element and append it to the result array
            next_element = arr[-1] ^ num
            arr.append(next_element)
        
        return arr

def decode(encoded: List[int], first: int) -> List[int]:
    return Solution().decode(encoded, first)