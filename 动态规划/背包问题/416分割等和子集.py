class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 题解，转化成01背包问题，从nums里面找到若干个物品，只能用一次，看看是否恰好等于target
        # target = sum(nums) // 2
        # dp[i][j] 代表从0-i里面挑选物品，能否使他们的和等于j

        # dp[i][j] = dp[i-1][j] or dp[j-nums[i]] j >= nums[i]
        #             dp[i-1][j] j < nums
        # 初始化：当i=0, 只有一个可以选就是第0个 所以dp[0][nums[0]] = True
        # 当j=0, 不选取就可以 直接全部都是True
        summ = sum(nums)
        if summ % 2 == 1:return False
        target = summ // 2
        max_n = max(nums)
        if max_n > target:return False
        if max_n == target:return True
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n)]
        # 初始化
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if j > nums[i]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i]]
            if dp[i][j]:
                return True
        return False