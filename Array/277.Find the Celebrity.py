"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


# Time Complexity : O(n). Two single loop
# Space Complexity: O(1). A variable

class Solution:
	# @param {int} n a party with n people
	# @return {int} the celebrity's label or -1
	def findCelebrity(self, n):
		candidate = 0

		for i in range(1, n):
			if Celebrity.knows(candidate, i): # if candidate knows i, current candidate is not a celebrity, i could be the candidate instead
				candidate = i

		# double check if the candidate is celebrity
		for i in range(n):
			if i == candidate:
				continue
			# if candidate knows i or i does NOT know candidate, return -1
			if Celebrity.knows(candidate, i) or not Celebrity.knows(i, candidate):
				return -1
		return candidate