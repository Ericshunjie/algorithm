class Solution:
    def canPartition(self, nums):
        length = len(nums)
        summ = sum(nums)
        if summ & 1 == 1:
            return False
        target = summ // 2
        dp = [[False] * (target + 1) for _ in range(length)]
        dp[0][0] = True
        if nums[0] == target:
            dp[0][target] == True
        for i in range(1, length):
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] | dp[i][j-nums[i]]
            if dp[i][target]:
                return True
        return dp[-2][-1]

s = Solution()
r = s.canPartition([1,2,5])
