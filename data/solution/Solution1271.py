import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def toHexspeak(self, num: str) -> str:
        # Convert the number to an integer and then to a hexadecimal string
        hex_num = hex(int(num))[2:].upper()
        
        # Replace '0' with 'O' and '1' with 'I'
        hex_num = hex_num.replace('0', 'O').replace('1', 'I')
        
        # Define the valid set of characters for Hexspeak
        valid_chars = {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}
        
        # Check if all characters in the hex_num are in the valid set
        if all(char in valid_chars for char in hex_num):
            return hex_num
        else:
            return "ERROR"

def toHexspeak(num: str) -> str:
    return Solution().toHexspeak(num)