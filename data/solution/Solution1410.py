import collections
import string
import math
import datetime


class Solution:
    def entityParser(self, text: str) -> str:
        # Define a dictionary to map HTML entities to their corresponding characters
        html_entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        
        # Iterate over the dictionary and replace each entity in the text
        for entity, char in html_entities.items():
            text = text.replace(entity, char)
        
        return text

def entityParser(text: str) -> str:
    return Solution().entityParser(text)