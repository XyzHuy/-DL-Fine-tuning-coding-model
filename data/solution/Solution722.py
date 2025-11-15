import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block_comment = False
        result = []
        buffer = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if line[i:i+2] == "*/":
                        in_block_comment = False
                        i += 1
                else:
                    if line[i:i+2] == "/*":
                        in_block_comment = True
                        i += 1
                    elif line[i:i+2] == "//":
                        break
                    else:
                        buffer.append(line[i])
                i += 1
            
            if not in_block_comment and buffer:
                result.append(''.join(buffer))
                buffer.clear()
        
        return result

def removeComments(source: List[str]) -> List[str]:
    return Solution().removeComments(source)