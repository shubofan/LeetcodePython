# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
	def rand10(self):
		"""
		:rtype: int
		"""
		# (rand_X() - 1) × Y + rand_Y() ==> 可以等概率的生成[1, X * Y]范围的随机数
		num = (rand7() - 1) * 7 + rand7();  # 等概率[1, 49]
		# 只要它还大于10，那就给我不断生成，因为我只要范围在1-10的，最后直接返回就可以了

		# (rand7() - 1) * 7 - > {0，7，14，21，28，35，42}
		# rand7() = {1,2,3,4,5,6,7}

		# (rand7() - 1) * 7 + rand7(); {1,2,3,4,5,6,7} + {8...14} + {15.....21} + {22....28} + {29....35} + {36....42} + {43........49} -> {1, .... ,49}
		while num > 10:
			num = (rand7() - 1) * 7 + rand7();

		return num;
