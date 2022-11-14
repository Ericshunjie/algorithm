class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # dp方法

        # dp[i,j] 为s1前i个和s2前j个能否交叉组成s3[i+j]

        # dp[i,j] = true if s1[i] == s3[i+j] and dp[i-1, j] is true
        #                 or s2[j] == s3[i+j] and dp[i,j-1] if True

        n1, n2, n3 = len(s1), len(s2), len(s3)
        print(n1,n2,n3)
        if n1 + n2 != n3: return False
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = 1

        for j in range(1, n2 + 1):
            if s2[j - 1] == s3[j - 1] and dp[0][j - 1] == 1:

                dp[0][j] = 1
        for i in range(1, n1 + 1):
            if s1[i - 1] == s3[i - 1] and dp[i - 1][0] == 1:
                print(i, j, dp[i][j])
                dp[i][0] = 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):

                if (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j] == 1) or (
                        s2[j - 1] == s3[i + j - 1] and dp[i][j - 1] == 1):
                    dp[i][j] = 1
                    print(i,j,dp[i][j])

        return dp[-1][-1] == 1



s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))