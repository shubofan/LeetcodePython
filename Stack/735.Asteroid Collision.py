class Solution:
	def asteroidCollision(self, asteroids: List[int]) -> List[int]:
		stack = []
		for i in asteroids:
			while stack and i < 0 < stack[-1]:  # only collide when stack move to right and i move to left
				if abs(stack[-1]) == abs(i):  # both i and stack[-1] explode , break the while loop, check next i
					stack.pop()
					break
				elif abs(stack[-1]) < abs(i):  # stack[-1] explode , continue check previous one
					stack.pop()
				else:  # abs(stack[-1]) > abs(i): i explode, break the while loop, check next i
					break
			else:  # empty or cannot collide
				stack += [i]

		return stack