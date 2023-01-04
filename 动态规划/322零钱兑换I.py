class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # dp[i] 表示凑成金额i所需要的最少硬币个数
        # dp[i] = min(dp[i-coin[j]]) + 1
        # 初始化
        # coins.sort()
        n = len(coins)
        if amount == 0:return 0
        dp = [amount * 2] * (amount + 1) #初始化一个最大值
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(n):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        return dp[-1] if dp[-1] != amount * 2 else -1

