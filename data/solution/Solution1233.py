import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders to ensure that parent folders come before subfolders
        folder.sort()
        
        # Initialize the result list with the first folder
        result = [folder[0]]
        
        # Iterate over the sorted folders starting from the second one
        for f in folder[1:]:
            # Check if the current folder is not a subfolder of the last folder in the result
            if not f.startswith(result[-1] + "/"):
                result.append(f)
        
        return result

def removeSubfolders(folder: List[str]) -> List[str]:
    return Solution().removeSubfolders(folder)