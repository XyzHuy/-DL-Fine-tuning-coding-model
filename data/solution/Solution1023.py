import random
import functools
import collections
import string
import math
import datetime


from typing import List
import re

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # Create a regex pattern from the given pattern
        # The regex will match if the query contains the pattern's characters in order
        # and any lowercase letters can be inserted between them
        regex_pattern = "^" + "[a-z]*".join(list(pattern)) + "[a-z]*$"
        
        # Compile the regex pattern for better performance
        compiled_pattern = re.compile(regex_pattern)
        
        # Check each query against the compiled regex pattern
        return [bool(compiled_pattern.match(query)) for query in queries]

# Example usage:
# solution = Solution()
# print(solution.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))  # Output: [True, False, True, True, False]
# print(solution.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"))  # Output: [False, True, True, False, False]
# print(solution.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT")) # Output: [False, True, False, False, False]

def camelMatch(queries: List[str], pattern: str) -> List[bool]:
    return Solution().camelMatch(queries, pattern)