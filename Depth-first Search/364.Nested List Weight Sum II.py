"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution:
	"""
	@param nestedList: a list of NestedInteger
	@return: the sum
	"""
# DFS

def depthSumInverse(self, nestedList):
    def getMaxDepth(nestedList):
        depth = 1
        for l in nestedList:
            if not l.isInteger():
                depth = max(depth, 1 + getMaxDepth(l.getList()))

        return depth

    def getSum(maxDepth, level, nestedList):
        res = 0
        for l in nestedList:
                if l.isInteger():
                    res += l.getInteger() * (maxDepth - level)
                else:
                    res += getSum(maxDepth, level+1, l.getList())
        return res

    maxDepth = getMaxDepth(nestedList)
    return getSum(maxDepth, 0, nestedList)

# BFS

# def depthSumInverse(self, nestedList):
#     res, levelSum = 0, 0
#     q = collections.deque()
#     q += [nestedList]

#     while q:
#         size = len(q)
#         for i in range(size):
#             lst = q.popleft()
#             for l in lst:
#                 if l.isInteger():
#                     levelSum += l.getInteger() # levelSum never get clear since outer integer need to be added multiple times
#                 else:
#                     q += [l.getList()]
#         res += levelSum

#     return res

