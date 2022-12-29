class Solution:
    def lastStoneWeightII(self, stones) -> int:
        ## 转化成01背包问题：书包的容量为 w=sum(stones) // 2 最终返回 dp[w] - w
        # dp[j] 为容量为j的书包可以装多重的石头

        n = len(stones)
        w = sum(stones) // 2
        dp = [0] * (w + 1)

        for i in range(n):
            for j in range(w, -1, -1):
                if j-stones[i] >= 0:
                    dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        print(dp)
        return abs(sum(stones) - dp[w]-dp[w])
s = Solution()
res = s.lastStoneWeightII([31,26,33,21,40])
print(res)
