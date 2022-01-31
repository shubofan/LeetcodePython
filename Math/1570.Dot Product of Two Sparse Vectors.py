class SparseVector:
	def __init__(self, nums):
		self.idxToNum = {i:num for i,num in enumerate(nums) if num != 0}

	def dotProduct(self, vec):
		res = 0
		for idx, num in vec.idxToNum.items():
			if idx in self.idxToNum:
				res += num * self.idxToNum[idx]

		return res



if __name__ == '__main__':
	nums1 = [0,1,0,0,2,0,0]
	nums2 = [1,0,0,0,3,0,4]
	v1 = SparseVector(nums1)
	v2 = SparseVector(nums2)
	print(v1.dotProduct(v2))
