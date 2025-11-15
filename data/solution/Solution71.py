import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/'
        components = path.split('/')
        stack = []
        
        for component in components:
            if component == '' or component == '.':
                # Ignore empty components and current directory marker '.'
                continue
            elif component == '..':
                # Pop the last directory if possible for parent directory marker '..'
                if stack:
                    stack.pop()
            else:
                # Add valid directory or file name to the stack
                stack.append(component)
        
        # Join the stack to form the simplified path
        simplified_path = '/' + '/'.join(stack)
        return simplified_path

def simplifyPath(path: str) -> str:
    return Solution().simplifyPath(path)