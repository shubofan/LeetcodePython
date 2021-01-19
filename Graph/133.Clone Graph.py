"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = set()
        visited.add(node.val)

        # key is val of node, val is new node in new graph
        # dic[val] will return node in new graph.
        dic = {}
        s = [node]

        # DFS original graph
        while s:
            top = s.pop()
            # create new node if it has not been created before
            if top.val not in dic:
                newNode = Node(top.val)
                dic[top.val] = newNode

            for neighbor in top.neighbors:
                # create new node if it has not been created before
                if neighbor.val not in dic:
                    newNode = Node(neighbor.val)
                    dic[neighbor.val] = newNode
                # copy neighbors to current node's neighbors
                dic[top.val].neighbors += [dic[neighbor.val]]
                if neighbor.val not in visited:
                    s += [neighbor]
                    visited.add(neighbor.val)
        return dic[node.val]

