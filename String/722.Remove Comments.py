class Solution:
	def removeComments(self, source: List[str]) -> List[str]:
		res = []
		in_block = False  # if current char in /* */ comment block

		for s in source:
			i, n = 0, len(s)
			if not in_block:
				tem = ''
			# check each char of s
			while i < n:
				if i < n - 1 and s[i:i + 2] == '/*' and not in_block:  # find the start of block comment
					in_block = True
					i += 2
				elif i < n - 1 and s[i:i + 2] == '*/' and in_block:  # reach end of block comment when in_block == True
					in_block = False
					i += 2
				elif i < n - 1 and s[
				                   i:i + 2] == '//' and not in_block:  # meet // and not in the block comment, ignore every thing after it
					break
				elif not in_block and i < n:  # current char not in block, append it to tem
					tem += s[i]
					i += 1
				else:
					i += 1
			# if tem and s not block comment
			if tem and not in_block:
				res += [tem]

		return res