class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 动态规划
        # dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        # cost[i]的定义是从i向上爬需要支付的费用，cost的最后一个不是楼顶，所以dp的长度应该是n+1
        n = len(cost)
        dp = [0] * (n+1)
        if n <= 1:return 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]

# 动态规划五部曲：
# 1、确定dp数组及其下表的含义
# 2、确定递推公式
# 3、dp数组的边界是什么 也就是初始化
# 4、遍历的顺序
# 5、遍历推导计算dp table
