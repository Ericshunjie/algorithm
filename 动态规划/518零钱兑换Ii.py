class Solution:
    def change(self, amount: int, coins) -> int:

        ## 完全背包问题 w = amout val=coins 装满容量为amout的背包有多少总方法
        # dp[j] 容量为j的背包有多少种方法
        # dp[j] = max(dp[j], dp[j-val[i]] + 1) !! 错 这样返回的结果有重复 最终的结果是排列数
        # dp[j] += dp[j-coins[i]] for i
        # dp[0] = 1
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(amount + 1):
                if j - coins[i] >= 0:
                    dp[j] += dp[j - coins[i]]
        return dp[-1]