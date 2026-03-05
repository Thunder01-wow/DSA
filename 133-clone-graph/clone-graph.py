"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]

            copy = Node(node.val)
            clone[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        
        if not node:
            return None
        
        return dfs(node)