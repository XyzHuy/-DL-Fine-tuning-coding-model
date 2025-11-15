import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # Helper function to generate strobogrammatic numbers of a given length
        def generate(length, isFinal):
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            
            middles = generate(length - 2, False)
            result = []
            for middle in middles:
                if not isFinal:
                    result.append("0" + middle + "0")
                result.append("1" + middle + "1")
                result.append("6" + middle + "9")
                result.append("8" + middle + "8")
                result.append("9" + middle + "6")
            return result
        
        # Count strobogrammatic numbers within the range
        def countStrobogrammatic(low, high):
            count = 0
            for length in range(len(low), len(high) + 1):
                for num in generate(length, True):
                    if (length == len(low) and num < low) or (length == len(high) and num > high):
                        continue
                    count += 1
            return count
        
        return countStrobogrammatic(low, high)

def strobogrammaticInRange(low: str, high: str) -> int:
    return Solution().strobogrammaticInRange(low, high)