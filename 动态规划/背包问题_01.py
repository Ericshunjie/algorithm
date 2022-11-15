# 01背包
# 有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
# 样例 w = 3, weight = [1,3,4],value = [15,20,30]
# 输出 35

# dp 问题
# 1、dp table dp[i][j] 代表从0-i物品里面任意取，放进容量为j的背包的价值总和最大值
# 2、递推 dp[i][j] = dp[i-1][j] 物品i不放入背包中
#     或者物品i 放入背包中 dp[i-1][j-weight[i]] + value[i]
# 3、初始化 dp[i][0]=0   dp[0][j]随着j增大 当j>=value[0]的时候 dp[0][j]开始等于1
class Solution():
    def bagproblem_01(self, w, weight, value):
        n = len(weight)
        dp = [[0] * (w + 1) for _ in range(n)]
        for j in range(1,w + 1):
            if j >= weight[0]:
                dp[0][j] = value[0]
        for i in range(1, n):
            for j in range(1, w + 1):
                if j - weight[i] >=0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)

        return dp[-1][-1]



# 一维写法 滚动数组
## 由于dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
# dp[i][j]都是在上一排的基础上计算得来 进一步可以变为dp[i][j] = max(dp[i][j], dp[i-1][j-weight[i]] + value[i])
# 将第i维去掉，dp[j] = max(dp[j], dp[j-weight[i] + value[i]])
# 1、dp[j]代表容量为j的背包的最大容纳价值
# 2、 dp[j] = max(dp[j], dp[j-weight[i] + value[i]])
# 3、初始化 dp[] = 0
# 4、遍历 for i in range(n): for j in range(w, -1, -1)

# class Solution():
#     def bagproblem_01(self,w, weight, value):
#         n = len(weight)
#         dp = [0] * (w + 1)
#         for i in range(n):
#             #为什么要反过来遍历，dp[j]的更新依赖于它前面的状态，如果先更新前面的，那个这个时候dp[j-weight[i]]就错误了，不是上一排的数据了；
#             for j in range(w,-1,-1):
#                 if j-weight[i] >= 0:
#                     dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
#         return dp[-1]

s = Solution()
res = s.bagproblem_01(4, [1,3,4],[15,20,30])
print(res)
