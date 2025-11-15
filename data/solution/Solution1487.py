import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_count = {}
        result = []
        
        for name in names:
            if name not in name_count:
                # If the name is not used, add it to the result and initialize its count
                result.append(name)
                name_count[name] = 1
            else:
                # If the name is used, find the smallest k such that name(k) is not used
                k = name_count[name]
                new_name = f"{name}({k})"
                while new_name in name_count:
                    k += 1
                    new_name = f"{name}({k})"
                # Add the new unique name to the result
                result.append(new_name)
                # Update the count for the original name and the new name
                name_count[name] = k + 1
                name_count[new_name] = 1
        
        return result

def getFolderNames(names: List[str]) -> List[str]:
    return Solution().getFolderNames(names)