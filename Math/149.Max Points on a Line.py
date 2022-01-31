class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        res = 0
        for i in range(l):
            dic = {'noslope': 1} # slope: number of points with same slope
            same = 0 # same points
            for j in range(i+1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]:
                    same += 1
                    continue
                if points[i][0]== tx:
                    slope = 'noslope' # No slope
                else:
                    slope = (points[i][1]-ty) * 1.0 / (points[i][0]-tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            res = max(res, max(dic.values()) + same)
        return res