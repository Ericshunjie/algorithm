class Solution:
    def findMinArrowShots(self, points) -> int:
        # 贪心 按照气球起始位置升序排列然后逐个区间计算
        # 注意：右边界是取当前区间的最小的
        points = sorted(points, key=lambda x:x[0])
        print(points)
        n = len(points)
        if n == 0:return 0
        result = 1
        for i in range(1, n):
            if points[i][0] > points[i-1][1]:
                # 当前左边界 大于 当前区间的右边界，重新起一个区间
                result += 1
            else:
                # 当前左边界 小于 当前区间的右边界，纳入区间，更新右边界，取二者最小的
                points[i][1] = min(points[i][1], points[i-1][1])
        return result