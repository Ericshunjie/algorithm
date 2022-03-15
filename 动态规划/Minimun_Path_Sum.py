class Solution:
    def minPathSum(self, grid) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return None
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for i in range(rows)]
        for i in range(rows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1,cols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1, rows):
            for j in range(1,cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]


# dp方程：
# dp[i+1, j + 1] = min(dp[i,j-1], dp[i-1,j]) + grid[i,j]
# dp[i,j]定义：从左上角到i,j的最小路径和