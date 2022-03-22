# 完全背包就是每件物品的个数是无数个
class Solution():
    def bagproblem_01(self,w, weight, value):
        n = len(weight)
        dp = [0] * (w + 1)
        for i in range(n):
            for j in range(w + 1): # 主要区别就是背包容量正向遍历
                if j-weight[i] >= 0:
                    dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
                print(i,j,dp)
        return dp[-1]

s = Solution()
res = s.bagproblem_01(4, [1,3,4],[15,20,30])
print(res)