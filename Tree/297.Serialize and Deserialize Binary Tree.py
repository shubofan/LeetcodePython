from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = ''
        if not root:
            return data
        q = deque()
        q += [root]
        while q:
            top = q.popleft()
            if top:
                data = data + str(top.val) + ','
                q += [top.left]
                q += [top.right]
            else:
                data = data + 'x,'
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        lst = data.split(',')
        q = deque()
        root = TreeNode(lst.pop(0))
        q += [root]
        while q:
            top = q.popleft()
            if lst:
                val = lst.pop(0)
                if val != 'x':
                    node = TreeNode(val)
                    top.left = node
                    q += [node]
            if lst:
                val = lst.pop(0)
                if val != 'x':
                    node = TreeNode(val)
                    top.right = node
                    q += [node]

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# n-ary-tree
# https://www.junhaow.com/lc/problems/tree/recovery-and-construction/428_serialize-and-deserialize-n-ary-tree.html