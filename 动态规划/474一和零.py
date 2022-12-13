class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def counts(s):
            ones = 0
            zeros = 0
            for char in s:
                if char == '0':
                    zeros += 1
                else:
                    ones += 1
            return zeros, ones
        # 传统的01背包问题有一个容量 但是这里有两个容量mn
        # 所以这里是一个三维背包问题dp[i][j][k] 代表前i个物体子集中最多有j个0 k个1的最大长度
        # 最终求dp[l][m][n]
        # dp[i][j][k] = max(dp[i-1][j][k],
        #                     dp[i-1][j-zeros][k-ones] + 1)
        l = len(strs)
        dp = [[[0] * (n+1) for _ in range(m+1)] for j in range(l+1)]
        for i in range(1, l+1):
            zeros,ones = counts(strs[i-1])
            for j in range(m+1):
                for k in range(n+1):
                    #不能把物体i放进去
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-zeros][k-ones] + 1)
        return dp[-1][-1][-1]
