# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(grid, row, column):
#             grid[row][column] = '0'
#             if (row-1) >= 0 and grid[row-1][column] == '1':
#                 dfs(grid, row-1, column)
#             if (row+1) < len(grid) and grid[row+1][column] == '1':
#                 dfs(grid, row+1, column)
#             if (column-1) >= 0 and grid[row][column-1] == '1':
#                 dfs(grid, row, column-1)
#             if (column+1) < len(grid[0]) and grid[row][column+1] == '1':
#                 dfs(grid, row, column+1)
#         if not grid:
#             return 0
#         rows = len(grid)
#         if not grid[0]:
#             return 0
#         columns = len(grid[0])
#         result = 0
#         for i in range(rows):
#             for j in range(columns):
#                 if grid[i][j] == '1':
#                     result += 1
#                     dfs(grid, i,j)
#         return result
# 遍历每一个点，遇到1就把结果加1 ，然后递归的把他上下左右的1 都变成0
# 深度优先递归 
# 尝试使用广度优先解决


class Solution:
    def numIslands(self, grid) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        self.rows = len(grid)
        self.cols = len(grid[0])

        p = [i for i in range(self.rows * self.cols)]
        zeros = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '1':
                    self._union(p, i, j, grid)
                else:
                    zeros += 1

        return len(set([self._find(p, i) for i in range(self.rows * self.cols)])) - zeros

    def _union(self, p, i, j, grid):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for k in range(4):
            ii, jj = i + dx[k], j + dy[k]
            if 0 <= ii < self.rows and 0 <= jj < self.cols and grid[ii][jj] == '1':
                p1 = self._find(p, ii * self.cols + jj)
                p2 = self._find(p, i * self.cols + j)
                if p1 != p2:
                    p[p1] = p2

    def _find(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != root:
            tmp = p[i]
            p[i] = root
            i = tmp
        return root
s = Solution()
r = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print(r)