class Solution:
    def numIslands(self, grid) -> int:
        def dfs(grid, row, column):
            grid[row][column] = '0'
            if (row-1) >= 0 and grid[row-1][column] == '1':
                dfs(grid, row-1, column)
            if (row+1) < len(grid) and grid[row+1][column] == '1':
                dfs(grid, row+1, column)
            if (column-1) >= 0 and grid[row][column-1] == '1':
                dfs(grid, row, column-1)
            if (column+1) < len(grid[0]) and grid[row][column+1] == '1':
                dfs(grid, row, column+1)
        if not grid:
            return 0
        rows = len(grid)
        if not grid[0]:
            return 0
        columns = len(grid[0])
        result = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    result += 1
                    dfs(grid, i,j)
        return result
# 遍历每一个点，遇到1就把结果加1 ，然后递归的把他上下左右的1 都变成0
# 深度优先递归 
# 尝试使用广度优先解决