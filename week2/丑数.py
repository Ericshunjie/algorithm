class Solution:
    def nthUglyNumber(self, n: int) -> int:

        dp = [1]
        a,b,c = 0,0,0
        for i in range(1, n):
            n2, n3, n5 = 2*dp[a], 3*dp[b], 5*dp[c]
            n = min(n2,n3,n5)
            dp.append(n)
            if n == n2: a+=1
            if n == n3: b+=1
            if n == n5: c+=1
        return dp[-1]

"""
方法：动态规划

"""