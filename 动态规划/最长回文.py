class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 回文子串 dp问题
        # dp[i,j]代表字符串s从i到j是否为回文子串，j-i+1就是长度
        # dp[i][j] = 1 if dp[i+1][j-1] and s[i] == s[j]
                        # or j-1==i and s[i]==s[j]
        n = len(s)
        if n <=1 :return s
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
            dp[i][i] = 1
        res = s[0]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j==i+1 or dp[i+1][j-1]:
                        dp[i][j] = 1
                        if j-i+1 > len(res):
                            res = s[i:j+1]
        return res
