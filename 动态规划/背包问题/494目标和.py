class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:

        ## 转化成01背包问题，假设 加法的和为x  减法的和就是（sum-x）
        #  x - (sum-x) = target ==> x = (sum+target) / 2
        ## 问题转化成：填满x的背包 有多少种方法 组合问题
        #  dp[j] 代表填满 容量为j的书包有多少种方法
        # dp[j] += dp[j-nums[i]]
        # dp[0]=1 dp[1:] =0
        n = len(nums)
        sum_nums = sum(nums)
        # (sum_nums + target) %2 == 1的话 不可能存在 return0
        if (sum_nums + target) % 2 == 1: return 0
        if abs(target) > sum_nums: return 0

        w = abs((sum_nums + target) // 2)
        dp = [0] * (w + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(w, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] += dp[j - nums[i]]
        return dp[-1]

s = Solution()
res = s.findTargetSumWays([0,0,0,0,0,0,0,0,1],1)
print(res)