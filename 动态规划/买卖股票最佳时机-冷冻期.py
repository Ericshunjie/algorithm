class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 状态：
        # 0：空仓 不是冷冻期 空仓 （今天没有操作）
        # 1：买入并持有
        # 2: 空仓 冷冻期 不能交易 今天卖出

        # dp[i][0] = max(dp[i-1][0], dp[i-1][2])            dp[0][0] = 0
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) dp[0][1] = -prices[0]
        # dp[i][2] = dp[i-1][1] + prices[i]                   dp[0][2] = 0
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]
            # dp[i][3] = dp[i-1][2]
        return max(dp[-1])
