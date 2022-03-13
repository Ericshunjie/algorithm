## 多多面试题，给定一系列的点，计算这些点围成多边形的面积
# 如果多边形是凸多边形，那么直接以v0为中心点，计算n-2个三角形面积即可
# 如果是非凸多边形，那么怎么办？使用三角形带符号的面积，使用向量的叉乘，其绝对值为面积
# 解决办法：以v0为起点，计算n-2个带符号的三角形面积相加即可

class Solution():
    def cal_area(self, pts):
        def get_area(v1, v2):
            return v1[0] * v2[1] - v1[1] * v2[0]


        n = len(pts)
        vectors = [[0,0] for i in range(n)]

        for i in range(n):
            vectors[i][0] = pts[i][0] - pts[0][0]
            vectors[i][1] = pts[i][1] - pts[0][1]

        area = 0
        for i in range(1, n - 1):
            area += get_area(vectors[i], vectors[i + 1]) / 2
        return area

s = Solution()
res = s.cal_area([[0,0],[1,1],[2,0],[2,1],[3,2],[3,3],[2,5],[1,4],[0,4]])
print(res)

