import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a set of all nodes
        all_nodes = set(range(n))
        # Create a set of nodes that have incoming edges
        nodes_with_incoming_edges = {to_node for _, to_node in edges}
        # The result is the set difference between all nodes and nodes with incoming edges
        return list(all_nodes - nodes_with_incoming_edges)

def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    return Solution().findSmallestSetOfVertices(n, edges)