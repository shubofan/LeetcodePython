# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        self.dic = {}
        for i in range(26):
            self.dic[i] = chr(97 + i)
        res = []
        self.dfs(root, '', res)
        res.sort()
        return res[0]

    def dfs(self, root: TreeNode, path: str, res: List):
        if root:
            lst = list(path)
            lst.insert(0, self.dic[root.val])
            path = ''.join(lst)
            if not root.left and not root.right:
                res += [path]
            else:
                self.dfs(root.left, path, res)
                self.dfs(root.right, path, res)