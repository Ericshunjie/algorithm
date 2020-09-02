class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            m = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    m = max(m, dp[j] + 1)
            dp[i] = m
        return max(dp)
s = Solution()
r = s.lengthOfLIS([10,9,2,5,3,7,101,18])
print(r)