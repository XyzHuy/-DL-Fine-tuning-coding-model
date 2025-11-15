import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # Dictionary to map file content to list of file paths
        content_to_paths = defaultdict(list)
        
        for path in paths:
            # Split the path into directory and files
            parts = path.split()
            directory = parts[0]
            
            # Process each file in the directory
            for file in parts[1:]:
                # Split the file name and content
                name, content = file.split('(')
                content = content[:-1]  # Remove the closing parenthesis
                # Construct full file path
                full_path = f"{directory}/{name}"
                # Append the file path to the list of paths for this content
                content_to_paths[content].append(full_path)
        
        # Filter out groups that have only one file (no duplicates)
        return [paths for paths in content_to_paths.values() if len(paths) > 1]

def findDuplicate(paths: List[str]) -> List[List[str]]:
    return Solution().findDuplicate(paths)