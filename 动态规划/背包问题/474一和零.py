class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # 三维维01背包问题
        # dp[i,j,k] = max(dp[i-1,j,k], dp[i-1,j-nums0[i],k-nums1[i]])
        def counts(s):
            ones, zeros = 0, 0
            for char in s:
                if char == '1':
                    ones += 1
                else:
                    zeros += 1
            return ones, zeros

        nn = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(nn + 1)]

        for i in range(nn):
            ones, zeros = counts(strs[i])
            # 三维情况下这里jk可以从0开始
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i + 1][j][k] = dp[i][j][k]
                    if j - zeros >= 0 and k - ones >= 0:
                        dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - zeros][k - ones] + 1)

        return dp[-1][-1][-1]


class Solution1(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        # 二维01背包问题
        # dp[j,k] = max(dp[j,k], dp[j-nums0[i],k-nums1[i]])
        def counts(s):
            ones, zeros = 0, 0
            for char in s:
                if char == '1':
                    ones += 1
                else:
                    zeros += 1
            return ones, zeros

        nn = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(nn):
            ones, zeros = counts(strs[i])
            # 二维状态下 必须是逆序
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j - zeros >= 0 and k - ones >= 0:
                        # print(i,j,k,ones,zeros)
                        dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)

        return dp[-1][-1]


s = Solution()
s.findMaxForm(["10","0001","111001","1","0"],5,3)