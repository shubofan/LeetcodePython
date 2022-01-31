# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
	"""
	:type robot: Robot
	:rtype: None
	"""

	def cleanRoom(self, robot):
		def dfs(x, y, seen, robot, direction):
			# going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
			dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
			seen.add((x, y))
			robot.clean()
			for i in range(4):
				n_direction = (direction + i) % 4
				nx, ny = x + dirs[n_direction][0], y + dirs[n_direction][1]
				if (nx, ny) not in seen and robot.move():  # continue to move to given direction
					dfs(nx, ny, seen, robot, n_direction)
					robot.turnRight()
					robot.turnRight()
					robot.move()
					robot.turnLeft()
					robot.turnLeft()
				robot.turnRight()  # cannot move, turn right (clockwise)

		# start from (0, 0) and direction is 0 -> move up
		dfs(0, 0, set(), robot, 0)


