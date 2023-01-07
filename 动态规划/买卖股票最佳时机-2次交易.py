class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][j] 代表第i天状态为j的最大收益
        # j = 0-4
        # 0：没有操作 空仓
        # 1：第一次持有
        # 2：第一次卖出
        # 3：第二次持有
        # 4：第二次卖出
        # dp[i][0] = 0
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) dp[0][1] = -prices[0]
        # dp[i][2] = max(dp[i-1][1] + prices[i], dp[i-1][2]) dp[0][2] = 0
        # dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[1]) dp[0][3] = -prices[0]
        # dp[i][4] = max(dp[i-1][3] + prices[i], dp[i-1][4]) dp[0][4] = 0
        n = len(prices)
        dp = [[0] * 5 for i in range(n)]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, n):
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][1] + prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][3] + prices[i], dp[i-1][4])
        return dp[-1][-1]
