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


# recursive
class Solution(object):
	# @param {NestedInteger[]} nestedList a list of NestedInteger Object
	# @return {int} an integer
	def depthSum(self, nestedList):
		def getSum(nestedList, level):
			res = 0

			for ni in nestedList:

				if ni.isInteger():
					res += ni.getInteger() * level
				else:
					res += getSum(ni.getList(), level + 1)
			return res

		return getSum(nestedList, 1)

# iterative
from collections import deque

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = deque([(nestedList, 1)])
        res = 0
        while q:
            aList, depth = q.popleft()
            for item in aList:
                if item.isInteger():
                    res += item.getInteger() * depth
                else:
                    q.append((item.getList(), depth + 1))
        return res