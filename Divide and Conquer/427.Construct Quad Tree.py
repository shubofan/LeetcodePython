
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List

# Time: O(N^2)， create a Node for each cell. recursive equation is T(N) = 4 * T(N/2). By master theorem, it is O(N^2).
# Space: O(logN)
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(grid, x1, x2, y1, y2):
            if x1 == x2 and y1 == y2:  # base case, just one square
                return Node(grid[x1][y1], True, None, None, None, None)

            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            # each time divide the original question of half of it
            top_left = build(grid, x1, mid_x, y1, mid_y)
            top_right = build(grid, x1, mid_x, mid_y + 1, y2)
            bottom_Left = build(grid, mid_x + 1, x2, y1, mid_y)
            bottom_right = build(grid, mid_x + 1, x2, mid_y + 1, y2)

            # all the children are leaf and have same value,  set val to the value of the grid and set the four children to Null and stop.
            if top_left.val == top_right.val == bottom_Left.val == bottom_right.val and top_left.isLeaf and top_right.isLeaf and bottom_Left.isLeaf and bottom_right.isLeaf:
                return Node(top_left.val, True, None, None, None, None)
            else:
                # current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids
                return Node(top_left.val, False, top_left, top_right, bottom_Left, bottom_right)

        x1, x2 = 0, len(grid) - 1
        y1, y2 = 0, len(grid[0]) - 1

        return build(grid, x1, x2, y1, y2)