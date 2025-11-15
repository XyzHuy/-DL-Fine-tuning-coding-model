import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize an array to store the multiplication results
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both strings to facilitate multiplication from least significant digit
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Perform multiplication digit by digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                # Add the product to the corresponding position in the result array
                result[i + j] += product
                # Handle carry over
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Remove leading zeros and convert the result array back to a string
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert the result array to a string
        return ''.join(map(str, result[::-1]))

def multiply(num1: str, num2: str) -> str:
    return Solution().multiply(num1, num2)