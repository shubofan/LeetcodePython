"""
Definition for a directed graph node

"""
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

'''
       1
    3  2  4 
   5 6   

serializedTree:  1,3,3,2,5,0,6,0,2,0,4,0, 
'''


class Solution:
    def serialize(self, nodes):
        self.serializedTree = ''  # 1,3,3,2,5,0,6,0,2,0,4,0,  l[0] root val. l[1] size of children
        if not nodes:
            return self.serializedTree

        root = nodes[0]
        self.serialize_helper(root)
        print(self.serializedTree)
        return self.serializedTree

    def serialize_helper(self, root):

        self.serializedTree += (str(root.label) + ',')
        self.serializedTree += (str(len(root.neighbors)) + ',')

        for i in range(len(root.neighbors)):
            self.serialize_helper(root.neighbors[i])

    def deserialize(self, data):
        if not data:
            return None
        lst = data.split(',')
        return self.deserialize_helper(lst)

    def deserialize_helper(self, lst):
        if not lst:
            return None

        label = int(lst.pop(0))
        root = DirectedGraphNode(label)

        neighbors_size = int(lst.pop(0))
        root.neighbors = []

        for i in range(neighbors_size):
            root.neighbors.append(self.deserialize_helper(lst))
        return root
