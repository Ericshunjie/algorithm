class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] 表示si 到 sj 是不是一个回文子串
        # if i == j:dp[i][j] = 1
        # if s[i] == s[j]: dp[i][j] = dp[i+1][j-1]
        n = len(s)
        if not n:return 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        res = n
        for i in range(n,-1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if i == j - 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    res += 1
        return res
s = Solution()
r = s.countSubstrings("aaa")
print(r)