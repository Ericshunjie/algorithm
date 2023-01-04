class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 组合数问题 dp[j] += dp[j-coins[i]]
        # 这是一个完全背包问题，每个物体可以取无数次
        # 如果外层循环是背包容量，则会造成重复计数
        # 外层循环必须先是物体
        # 举个例子 amount=3 coins=[1,2]
        # 如果先遍历背包容量 dp3=dp2 + dp1  =3   这种情况就存在重复统计了 [111,21,12]
        #                     dp2 = dp1+dp0 = 2
        #                     dp1 = 1 dp0 = 1
        # 如果先遍历物品 i=0 dp1 = 0 + dp0 = 1
        #                     dp2 = 0 + dp1 = 1
        #                     dp3 = 0 + dp2 = 1
        #                 i=1 dp1 = 1
        #                     dp2 = 1 + dp0 = 2
        #                     dp3 = 1 + dp1 = 2

        n = len(coins)
        if amount < 1: return 1
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] += dp[j - coins[i]]
        return dp[-1]