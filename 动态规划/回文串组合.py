class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # dp[i,j] 代表i到j是否为回文串
        # dp[i,j] = 1 if dp[i+1,j-1] == 1 and s[i] == s[j]
        for i in range(n - 2, -1, -1):

            for j in range(i + 1, n):

                if s[i] == s[j]:
                    if i == j - 1 or dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
        # print(dp)
        def dfs(i, res):
            # print(i,res)
            if i == n:
                result.append(res)
                return

            for j in range(i, n):
                if dp[i][j] == 1:
                    dfs(j+1, res + [s[i:j+1]])

        result = []
        dfs(0, [])
        return result
s = Solution()
res = s.partition('aab')
print(res)


