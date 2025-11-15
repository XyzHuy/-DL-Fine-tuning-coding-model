import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isValid(self, code: str) -> bool:
        import re
        
        # Regular expression to match CDATA content
        cdata_pattern = re.compile(r'<!\[CDATA\[.*?\]\]>')
        # Regular expression to match a valid tag
        tag_pattern = re.compile(r'<([A-Z]{1,9})>[^<]*</\1>')
        
        # Remove all CDATA sections
        code = cdata_pattern.sub('#', code)
        
        # Continuously remove valid tags until no more can be removed
        while re.search(tag_pattern, code):
            code = tag_pattern.sub('#', code)
        
        # After all valid tags and CDATA sections are removed, the code should be empty or just '#'
        return code == '#'

def isValid(code: str) -> bool:
    return Solution().isValid(code)