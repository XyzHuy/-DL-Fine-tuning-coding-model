import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        # Create a dictionary to store the index of each feature
        feature_index = {feature: i for i, feature in enumerate(features)}
        
        # Create a dictionary to count the occurrences of each feature in the responses
        feature_count = defaultdict(int)
        
        # Process each response
        for response in responses:
            # Use a set to avoid counting the same feature multiple times in a single response
            seen_features = set(response.split())
            for feature in seen_features:
                if feature in feature_index:
                    feature_count[feature] += 1
        
        # Sort the features based on their count (descending) and original index (ascending)
        sorted_features = sorted(features, key=lambda x: (-feature_count[x], feature_index[x]))
        
        return sorted_features

def sortFeatures(features: List[str], responses: List[str]) -> List[str]:
    return Solution().sortFeatures(features, responses)