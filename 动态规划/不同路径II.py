class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[1] * cols for _ in range(rows)]
        if obstacleGrid[0][0] == 1:return 0
        for i in range(1, rows):
            dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
        for i in range(1,cols):
            dp[0][i] = 0 if obstacleGrid[0][i] == 1 else dp[0][i-1]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = 0 if obstacleGrid[i][j] == 1 else dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
