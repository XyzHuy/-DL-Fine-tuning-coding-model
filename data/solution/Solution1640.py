import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Create a dictionary to map the first element of each piece to the piece itself
        piece_dict = {piece[0]: piece for piece in pieces}
        
        # Initialize an index to traverse the arr
        index = 0
        
        # Traverse the arr
        while index < len(arr):
            # Check if the current element of arr is a key in piece_dict
            if arr[index] in piece_dict:
                # Get the corresponding piece
                piece = piece_dict[arr[index]]
                # Check if the piece matches the subarray of arr starting at the current index
                if arr[index:index + len(piece)] == piece:
                    # If it matches, move the index forward by the length of the piece
                    index += len(piece)
                else:
                    # If it does not match, return False
                    return False
            else:
                # If the current element of arr is not a key in piece_dict, return False
                return False
        
        # If we have successfully traversed the entire arr, return True
        return True

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    return Solution().canFormArray(arr, pieces)