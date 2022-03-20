class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        # 类似01背包问题
        # dp[i][j] 为最多又i个0 j个1的最大子集数
        # dp[i][j] = max(dp[i][j], dp[i-num0][j-num1] + 1)
        # dp[0][0] = 0

        nn = len(strs)
        nums0 = [0] * nn
        nums1 = [0] * nn
        dp = [[0] * (n+1) for _ in range(m+1)]
        print(len(dp),len(dp[0]))
        for i in range(nn):
            for s in strs[i]:
                if s == '0':
                    nums0[i] += 1
                else:
                    nums1[i] += 1
        print(nums0,nums1)
        for i in range(nn):
            for j in range(m,-1,-1):
                for k in range(n,-1,-1):
                    print(i,j,k)
                    if j-nums0[i] >= 0 and k-nums1[i] >= 0:
                        print(j-nums0[i],k-nums1[i])
                        print(dp[j][k])
                        print(dp[j-nums0[i]][k-nums1[i]])
                        dp[j][k] = max(dp[j][k], dp[j-nums0[i]][k-nums1[i]] + 1)
        return dp[-1][-1]

s = Solution()
s.findMaxForm(["10","0001","111001","1","0"],5,3)