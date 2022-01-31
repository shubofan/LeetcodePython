# Time complexity: O(max(N,M)), whereN and M are lengths of the input strings respectively. It's a one-pass solution.

# Space complexity: O(M + N)

class Solution:
	def compareVersion(self, version1: str, version2: str) -> int:
		v1, v2 = version1.split('.'), version2.split('.')

		# assume len(version1) > len(version2)
		if len(v1) < len(v2):
			return self.compareVersion(version2, version1) * -1

		l1 = len(v1)
		l2 = len(v2)

		for i in range(l2):
			if int(v1[i]) < int(v2[i]):
				return -1
			elif int(v1[i]) > int(v2[i]):
				return 1

		for i in range(l2, l1):
			if int(v1[i]) != 0:
				return 1
		return 0