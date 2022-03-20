class Solution:
    def merge(self, intervals):

        n = len(intervals)
        if n == 1:return intervals
        intervals = sorted(intervals, key=lambda x:x[0])
        result = []
        start,end = intervals[0]
        for i in range(n):
            if intervals[i][0] > end:
                result.append([start, end])
                start, end = intervals[i]
            else:
                end = max(end, intervals[i][1])
        result.append([start, end])
        return result

s = Solution()
res = s.merge([[1,3],[2,6],[8,10],[15,18]])
print(res)