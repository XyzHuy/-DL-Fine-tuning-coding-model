import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # The maximum number of "AA" and "BB" we can use is the minimum of x and y, 
        # because we need to alternate them to avoid "AAA" or "BBB".
        # We can always use all "AB" strings.
        max_aa_bb_pairs = min(x, y)
        # Each "AA" or "BB" contributes 2 to the length.
        length_from_aa_bb = max_aa_bb_pairs * 4
        # If x and y are not equal, we can add one more "AA" or "BB" at the end.
        if x != y:
            length_from_aa_bb += 2
        # Each "AB" contributes 2 to the length.
        length_from_ab = z * 2
        # The total maximum length is the sum of the lengths from "AA"/"BB" and "AB".
        return length_from_aa_bb + length_from_ab

def longestString(x: int, y: int, z: int) -> int:
    return Solution().longestString(x, y, z)