# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N), O(N)
# class BSTIterator:

#     def __init__(self, root: TreeNode):
#         self.res = []
#         stack = []
#         while root or stack:
#             if root:
#                 stack += [root]
#                 root = root.left
#             else:
#                 cur = stack.pop()
#                 self.res += [cur.val]
#                 if cur.right:
#                     root = cur.right
#         self.res.reverse()


#     def next(self) -> int:
#         if self.hasNext():
#             return self.res.pop()

#     def hasNext(self) -> bool:
#         return len(self.res) > 0

# Time O(1), Space O(h), h is the height of tree
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack += [root]
            root = root.left

    def next(self) -> int:
        if self.hasNext():
            cur = self.stack.pop()
            root = cur.right
            while root:
                self.stack += [root]
                root = root.left

        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()