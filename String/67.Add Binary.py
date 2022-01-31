# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         la, lb = list(a), list(b)

#         if len(la) < len(lb):
#             return self.addBinary(b, a)

#         # la >= lb

#         while len(la) > len(lb):
#             lb.insert(0, '0')
#         # print(la, lb)
#         # la.reverse()
#         # lb.reverse()
#         # print(la, lb)
#         res = []
#         carry = 0
#         for i in range(len(la)-1,-1,-1):
#             a, b = la[i], lb[i]
#             if carry == 1:
#                 if a == '0' and b == '0':
#                     res += ['1']
#                     carry = 0
#                 if a == '1' and b == '0' or a == '0' and b == '1':
#                     res += ['0']
#                     carry = 1

#                 if a == '1' and b == '1':
#                     res += ['1']
#                     carry = 1
#             else:
#                 if a == '0' and b == '0':
#                     res += ['0']
#                     carry = 0
#                 if a == '1' and b == '0' or a == '0' and b == '1':
#                     res += ['1']
#                     carry = 0

#                 if a == '1' and b == '1':
#                     res += ['0']
#                     carry = 1
#         if carry:
#             res += ['1']
#         # print(res)
#         return str(int(''.join(res[::-1])))

class Solution:
	def addBinary(self, a: str, b: str) -> str:
		la, lb = list(a), list(b)
		res = ''
		carry = 0
		while la or lb:
			sum_ = carry
			if la:
				sum_ += int(la.pop())
			if lb:
				sum_ += int(lb.pop())

			res += str(sum_ % 2)
			carry = sum_ // 2
		if carry:
			res += '1'
		return res[::-1]
