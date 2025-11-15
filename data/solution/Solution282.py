import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(index, path, value, prev):
            # If we have reached the end of the string and the value equals the target, add to result
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            
            # Try all possible splits of the remaining string
            for i in range(index + 1, len(num) + 1):
                # Extract the current number
                current_str = num[index:i]
                current_num = int(current_str)
                
                # If the current number starts with a zero, skip to avoid numbers with leading zeros
                if i != index + 1 and num[index] == '0':
                    break
                
                # If this is the first number in the path, just add it
                if index == 0:
                    backtrack(i, current_str, current_num, current_num)
                else:
                    # Addition
                    backtrack(i, path + '+' + current_str, value + current_num, current_num)
                    # Subtraction
                    backtrack(i, path + '-' + current_str, value - current_num, -current_num)
                    # Multiplication
                    # prev is the previous operand, which we multiply with current_num
                    # We subtract prev from value to remove its effect, then add prev * current_num
                    backtrack(i, path + '*' + current_str, value - prev + prev * current_num, prev * current_num)
        
        result = []
        backtrack(0, "", 0, 0)
        return result

def addOperators(num: str, target: int) -> List[str]:
    return Solution().addOperators(num, target)