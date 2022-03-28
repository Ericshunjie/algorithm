# 打家劫舍I的复杂版，房子收尾连接 收尾不能同时偷
# 将nums 分成nums[:n-1] nums[1:]两个单独的 就成了打家劫舍I的问题了


class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_range(nums):
            n = len(nums)
            pre, now = 0, nums[0]
            for i in range(1, n):
                now, pre = max(now, pre + nums[i]), now
            return now

        if len(nums) <= 2: return max(nums)
        return max(rob_range(nums[:len(nums) - 1]), rob_range(nums[1:]))