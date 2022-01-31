# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # Time complexity : O(logN). first to search the node to delete (O(H1) time complexity as already discussed )  H1 is a tree height from the root to the node to delete. Delete process takes O(H2) time, where H2 is a tree height from the root to delete to the leafs.
    # That in total results in O(H1+H2)=O(H) time complexity, where H is a tree height, equal to logN in the case of the balanced tree.

    # Space complexity : O(H)=O(LogN)to keep the recursion stack, where H is a tree height. H=logN for the balanced tree.
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key == root.val:
            # root is leaf
            if not root.left and not root.right:
                return None
            # just have right child
            elif not root.left:
                return root.right
            # just have right child
            elif not root.right:
                return root.left
            # found the node with min value of right subtree. root's left subtree should be the left subtree of it. New root is root's right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        return root
