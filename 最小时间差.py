class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def cal_diff(x, y):
            x1 = int(x[:2]) * 60 + int(x[3:5])
            x2 = int(y[:2]) * 60 + int(y[3:5])
            diff = abs(x2 - x1)
            diff = min(diff, 24 * 60 - diff)
            return diff

        timePoints.sort()
        n = len(timePoints)
        res = 24 * 60
        for i in range(n - 1):
            res = min(res, cal_diff(timePoints[i], timePoints[i + 1]))
        #首尾时间差要考虑进去
        res = min(res, cal_diff(timePoints[0], timePoints[-1]))
        return res