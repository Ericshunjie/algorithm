class Solution:
    def integerBreak(self, n: int) -> int:
        ## dp 问题
        # 1 确定dp table  dp[i]代表拆分i的最大乘积
        # 2 状态转移方程  for j in 1-(j-1) 取 dp[i] = max(j * (i-j), j*dp[i-j])
        #   要么拆j要么不拆j
        # 初始化dp[0,1]无意义 dp[2]=1

        dp = [1] * (n+1)
        for i in range(3, n+1):

            for j in range(1, i):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        return dp[-1]