import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Initialize an empty list to build the result string
        result = []
        # Initialize a pointer for the spaces list
        space_index = 0
        # Iterate over each character in the string s
        for i in range(len(s)):
            # If the current index matches the next space index, add a space
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            # Add the current character to the result
            result.append(s[i])
        # Join the list into a string and return
        return ''.join(result)

def addSpaces(s: str, spaces: List[int]) -> str:
    return Solution().addSpaces(s, spaces)