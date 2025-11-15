import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Create a dictionary to store the substitution table
        substitution_table = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        seen_letters = set()
        
        # Fill the substitution table with the first appearance of each letter in the key
        j = 0
        for char in key:
            if char != ' ' and char not in seen_letters:
                substitution_table[char] = alphabet[j]
                seen_letters.add(char)
                j += 1
                if j == 26:  # If we have mapped all 26 letters, we can stop
                    break
        
        # Decode the message using the substitution table
        decoded_message = []
        for char in message:
            if char == ' ':
                decoded_message.append(' ')
            else:
                decoded_message.append(substitution_table[char])
        
        return ''.join(decoded_message)

def decodeMessage(key: str, message: str) -> str:
    return Solution().decodeMessage(key, message)