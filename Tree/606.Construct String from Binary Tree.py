# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def tree2str(self, t: TreeNode) -> str:
    # if not t:
    #     return ''
    # # leaf
    # if not t.left and not t.right:
    #     return str(t.val)
    # # root with just left
    # if not t.right:
    #     return str(t.val) + '(' + self.tree2str(t.left) + ')'
    # # root with both left and right or just
    # return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'

    def tree2str(self, t: TreeNode) -> str:
        res = ''
        if not t:
            return res
        stack = [t]
        visited = set()

        while stack:
            cur = stack[-1]
            if cur in visited:
                stack.pop()
                res += ')'
            else:
                visited.add(cur)
                res = res + '(' + str(cur.val)
                if cur.right and not cur.left:
                    res += '()'

                if cur.right:
                    stack += [cur.right]

                if cur.left:
                    stack += [cur.left]
        return res[1: len(res) - 1]