class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        # 贪心 要求移除最小区间的数量 就是要求不重叠区间的数量w  n-w即为所求
        # 排序 +遍历
        # 按照右边界排序 就从左边开始遍历：想要让右边剩下的区间更多 这也是为什么用右边界排序

        n = len(intervals)
        if n <= 1:return 0
        intervals = sorted(intervals, key=lambda x:x[1])
        end = intervals[0][1]
        result = 1

        for i in range(1, n):
            if intervals[i][0] >= end:
                # 更新新的不重叠区间右边界
                result += 1
                end = intervals[i][1]
        return n - result


