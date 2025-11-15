import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings by the dot
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        
        # Get the maximum length of the two revision lists
        max_length = max(len(revisions1), len(revisions2))
        
        # Compare each revision
        for i in range(max_length):
            # Convert the current revision to integer, default to 0 if the revision is missing
            rev1 = int(revisions1[i]) if i < len(revisions1) else 0
            rev2 = int(revisions2[i]) if i < len(revisions2) else 0
            
            # Compare the current revisions
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        # If all revisions are equal
        return 0

def compareVersion(version1: str, version2: str) -> int:
    return Solution().compareVersion(version1, version2)