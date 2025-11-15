import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort the products lexicographically
        products.sort()
        
        # Initialize the result list
        result = []
        
        # Initialize the prefix
        prefix = ""
        
        # Iterate over each character in searchWord
        for char in searchWord:
            # Update the prefix
            prefix += char
            
            # Filter products that start with the current prefix
            products = [product for product in products if product.startswith(prefix)]
            
            # Add the first three products (if available) to the result
            result.append(products[:3])
        
        return result

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    return Solution().suggestedProducts(products, searchWord)