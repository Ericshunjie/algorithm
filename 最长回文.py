class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if s[i,j]是回文子串 并且 s[i-1] ==s[j +1]
        # 则 s[i-1, j+1]是回文子串
        n = len(s)
        if n == 1:return s
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        length = 1
        result = s[0]
        for i in range(n - 2, -1 , -1):
            for j in range(i + 1, n):
                if j == i + 1 and s[i] == s[j]:
                    dp[i][j] = 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                if dp[i][j] and j - i + 1 > length:
                    result = s[i:j+1]
        return result

s = Solution()
s.longestPalindrome("aacabdkacaa")