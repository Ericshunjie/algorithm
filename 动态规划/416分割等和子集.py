class Solution:
    def canPartition(self, nums) -> bool:
        # 转化成01背包问题 背包重量为w= sum(nums) // 2 重量和价值都是nums
        # 目的是看 dp[w] == w
        sums = sum(nums)
        if sums % 2 == 1:return False
        w = sums // 2
        n = len(nums)
        dp = [0] * (w + 1)

        for i in range(n):
            for j in range(w,-1,-1):
                if j - nums[i] >= 0:
                    dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[w] == w



