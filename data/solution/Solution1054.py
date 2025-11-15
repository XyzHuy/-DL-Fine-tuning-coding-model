import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Count the frequency of each barcode
        count = Counter(barcodes)
        # Sort barcodes by frequency (descending) and by value (ascending) for tie-breaking
        barcodes_sorted = sorted(barcodes, key=lambda x: (-count[x], x))
        
        # Result array to store the rearranged barcodes
        result = [0] * len(barcodes)
        # Place the most frequent barcodes in even indices first
        index = 0
        for barcode in barcodes_sorted:
            if index >= len(barcodes):
                index = 1  # Switch to odd indices if even indices are filled
            result[index] = barcode
            index += 2
        
        return result

def rearrangeBarcodes(barcodes: List[int]) -> List[int]:
    return Solution().rearrangeBarcodes(barcodes)