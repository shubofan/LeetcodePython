class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #         merged = []
        #         if not points:
        #             return len(merged)

        #         points = sorted(points, key=lambda x: x[0])

        #         for point in points:
        #             if not merged or point[0] > merged[-1][1]:
        #                 merged += [point]
        #             else:
        #                 start = max(point[0], merged[-1][0])
        #                 end = min(point[1], merged[-1][1])
        #                 merged.pop(0)
        #                 merged += [[start, end]]

        #         return len(merged)

        if not points:
            return 0
        points.sort(key=lambda x: x[0])
        # count of shoot
        count = 1

        # track the right boundry
        right = points[0][1]

        for i in range(1, len(points)):
            point = points[i]
            # if current right boundry < next point left, we NEED a new arrow and update the right boundry
            if right < point[0]:
                count += 1
                right = point[1]

            # if current right boundry >= next point left AND right boundry < next point right, we NEED to narrow down right boundry
            elif right > point[1]:
                right = point[1]
        return count
