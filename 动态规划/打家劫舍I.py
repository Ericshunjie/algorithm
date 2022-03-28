class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] 到第i个房间能得到的最高金额
        # dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # dp[0] = nums[0] dp[1] = max(nums[0], nums[1])
        n = len(nums)
        if n <= 1: return nums[0]
        dp = nums[:]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]