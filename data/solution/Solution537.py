import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Parse the first complex number
        real1, imaginary1 = num1[:-1].split('+')
        real1, imaginary1 = int(real1), int(imaginary1)
        
        # Parse the second complex number
        real2, imaginary2 = num2[:-1].split('+')
        real2, imaginary2 = int(real2), int(imaginary2)
        
        # Calculate the real part of the result
        real_result = real1 * real2 - imaginary1 * imaginary2
        
        # Calculate the imaginary part of the result
        imaginary_result = real1 * imaginary2 + imaginary1 * real2
        
        # Return the result in the required format
        return f"{real_result}+{imaginary_result}i"

def complexNumberMultiply(num1: str, num2: str) -> str:
    return Solution().complexNumberMultiply(num1, num2)