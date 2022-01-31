import collections
# Time complexity : O(m*n) where m is the row of the chessboard and n is column of the chessboard.

def minKnightMoves(self, x: int, y: int) -> int:
	# 8 directions
	directions = {(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)}

	visited = set()

	# Notice that the problem is symmetrical, that is the number of
	# steps to get to -10, -45 is the same as 10, 45.
	x, y = abs(x), abs(y)
	if x == 1 and y == 1: return 2 # cornel case

	# (x,y,steps)
	queue = collections.deque([(0, 0, 0)])
	while queue:
		cur_x, cur_y, steps = queue.popleft()
		if [cur_x, cur_y] == [x, y]: return steps

		for dx, dy in directions:
			if 0 <= cur_x + dx <= 300 and 0 <= cur_y + dy <= 300 and (cur_x + dx, cur_y + dy) not in visited:
				visited.add((cur_x + dx, cur_y + dy))
				queue.append((cur_x + dx, cur_y + dy, steps + 1))