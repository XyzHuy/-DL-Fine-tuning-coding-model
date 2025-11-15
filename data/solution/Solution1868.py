import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        
        while i < len(encoded1) and j < len(encoded2):
            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]
            
            min_freq = min(freq1, freq2)
            product = val1 * val2
            
            # If the result is not empty and the last value is the same as the current product, merge them
            if result and result[-1][0] == product:
                result[-1][1] += min_freq
            else:
                result.append([product, min_freq])
            
            # Decrease the frequency by the minimum frequency and move to the next segment if frequency becomes zero
            encoded1[i][1] -= min_freq
            if encoded1[i][1] == 0:
                i += 1
            
            encoded2[j][1] -= min_freq
            if encoded2[j][1] == 0:
                j += 1
        
        return result

def findRLEArray(encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
    return Solution().findRLEArray(encoded1, encoded2)