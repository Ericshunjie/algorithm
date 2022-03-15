class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        n = len(s)
        dp = [[0] * len(s) for i in range(n)]
        res = ''
        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j]:
                    dp[i][j] = 1 if j - i < 2 or dp[i+1][j-1] else 0
                else:
                    dp[i][j] = 0

                if dp[i][j] and j-i+1 > len(res):
                    res = s[i:j+1]
        return res
s = Solution()
r = s.longestPalindrome("babad")
print(r)





# dp[i,j] = dp[i+1, j-1] if s[i] == s[j]
# dp代表从i到j是否是回文子串