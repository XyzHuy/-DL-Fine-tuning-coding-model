import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        # Convert dig list to a set for O(1) lookups
        dug_cells = set((r, c) for r, c in dig)
        
        # Initialize the count of extractable artifacts
        extractable_artifacts = 0
        
        # Iterate over each artifact
        for r1, c1, r2, c2 in artifacts:
            # Assume the artifact can be extracted
            can_extract = True
            
            # Check each cell in the artifact's bounding box
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    # If any cell is not dug, the artifact cannot be extracted
                    if (r, c) not in dug_cells:
                        can_extract = False
                        break
                if not can_extract:
                    break
            
            # If the artifact can be extracted, increment the count
            if can_extract:
                extractable_artifacts += 1
        
        return extractable_artifacts

def digArtifacts(n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
    return Solution().digArtifacts(n, artifacts, dig)