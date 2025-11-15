import random
import functools
import collections
import string
import math
import datetime


import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans = []
        root = TrieNode()
        subtreeToNodes: dict[str, List[TrieNode]] = collections.defaultdict(list)

        # Construct the Trie
        for path in sorted(paths):
            node = root
            for s in path:
                node = node.children.setdefault(s, TrieNode())

        # For each subtree, fill in the {subtree encoding: [root]} hash table
        def buildSubtreeToRoots(node: TrieNode) -> str:
            subtree = '(' + ''.join(s + buildSubtreeToRoots(node.children[s])
                                    for s in node.children) + ')'
            if subtree != '()':
                subtreeToNodes[subtree].append(node)
            return subtree

        buildSubtreeToRoots(root)

        # Mark nodes that should be deleted
        for nodes in subtreeToNodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Construct the answer array for nodes that haven't been deleted
        def constructPath(node: TrieNode, path: List[str]) -> None:
            for s, child in node.children.items():
                if not child.deleted:
                    constructPath(child, path + [s])
            if path:
                ans.append(path)

        constructPath(root, [])
        return ans

def deleteDuplicateFolder(paths: List[List[str]]) -> List[List[str]]:
    return Solution().deleteDuplicateFolder(paths)