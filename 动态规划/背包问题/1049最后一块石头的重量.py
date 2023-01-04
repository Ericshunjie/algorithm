class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 本题任意选两块石头粉碎 返回最小的可能重量
        # 就是将石头分成两堆A和B，A-B即为返回最小重量，sum=A+B ret=sum-2*B
        # 要使ret 最小 就是使B最大
        # 问题转化成 背包问题 容量为w的背包最多能装多重的石头
        # 这里容量==重量  B不可能超过sum//2 所以w = sum//2
        n = len(stones)
        summ = sum(stones)
        w = summ // 2
        dp = [0] * (w + 1)

        for i in range(n):
            for j in range(w,-1,-1):
                if j >= stones[i]:
                    dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return summ - 2 * dp[-1]
s = Solution()
res = s.lastStoneWeightII([31,26,33,21,40])
print(res)
