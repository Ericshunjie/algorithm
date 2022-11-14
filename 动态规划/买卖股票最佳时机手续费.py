class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # dp 问题
        # dp[i][0] 代表第i天结束，手里没有持有股票的最大利润
        # dp[i][1] 代表第i天结束，手里持有股票的最大利润
        # 状态转移方程
        # 手里没有：今天卖了，或者昨天没有 今天没买
        # dp[i][0] = max(dp[i-1][1] + prices[i]  - fee, dp[i-1][0])
        # 手里有： 今天买了，昨天有 今天没动
        # dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        # 初始：
        # dp[0][0] = 0 dp[0][1] = -prices[0]
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i] - fee, dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return max(dp[-1])