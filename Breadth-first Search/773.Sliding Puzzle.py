# Time & space: O(m * n * (m * n)!).
# There are at most 6! permutations
import collections


class Solution(object):
	def slidingPuzzle(self, board):

		R, C = len(board), len(board[0])
		start = ''

		# flatten the 2d array to single string
		for x in range(R):
			for y in range(C):
				start += str(board[x][y])

		queue = collections.deque([(start, start.index('0'), 0)])
		seen = set()

		target = '123450'
		seen.add(start)

		while queue:
			board, pos, level = queue.popleft()

			if board == target:
				return level

			for d in (-1, 1, -C, C):
				next_pos = pos + d
				if abs(next_pos // C - pos // C) + abs(
						next_pos % C - pos % C) != 1:  # pos 2 can not be move pos 3 , similarly pos 3 can not be move to pos 2
					continue

				if 0 <= next_pos < R * C:
					newboard = list(board)
					newboard[pos], newboard[next_pos] = newboard[next_pos], newboard[pos] # swap pos and next pos
					newboard_str = ''.join(newboard) # generate new board
					if newboard_str not in seen:
						seen.add(newboard_str)
						queue.append((newboard_str, next_pos, level + 1))

		return -1


