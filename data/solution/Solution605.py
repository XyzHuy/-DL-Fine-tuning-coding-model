import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, count = 0, 0
        while i < len(flowerbed):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the previous and next plots are also empty or out of bounds
                empty_prev = (i == 0) or (flowerbed[i - 1] == 0)
                empty_next = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both previous and next plots are empty, we can plant a flower here
                if empty_prev and empty_next:
                    flowerbed[i] = 1
                    count += 1
                    # If we have planted enough flowers, return True
                    if count >= n:
                        return True
            # Move to the next plot
            i += 1
        # If we have not planted enough flowers, return False
        return count >= n

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    return Solution().canPlaceFlowers(flowerbed, n)