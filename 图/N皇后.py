# class Solution():
#     def solveNQueens(self, n):
#         if n < 1:return []
#         self.result = []
#         self.cols = set()
#         self.pie = set()
#         self.na = set()
#         self.DFS(n, 0, [])
#
#         return self._generate_result()
#
#     def DFS(self, n, row, cur_state):
#         #递归终止recursion terminator
#         if row == n:
#
#             self.result.append(cur_state)
#             return
#         for col in range(n):#按照列逐个进行试探
#             if col in self.cols or row+col in self.pie or row - col in self.na:
#                 continue
#             #将第row行 第col列放一个皇后 添加 col\na\pie状态
#             self.cols.add(col)
#             self.pie.add(col + row)
#             self.na.add(row - col)
#             #到下一层
#             self.DFS(n, row + 1, cur_state + [col])
#
#             #恢复状态 试探row的下一个 col
#             self.cols.remove(col)
#             self.pie.remove(col + row)
#             self.na.remove(row - col)
#
#     def _generate_result(self, n):
#

# class Solution():
#     def solveNQueens(self, n):
#         def DFS(queens, xy_dif, xy_sum):
#             l = len(queens)
#             if l == n:
#                 result.append(queens)
#                 return
#             for col in range(n):
#                 if col not in queens and l + col not in xy_sum and l - col not in xy_dif:
#                     DFS(queens+[col], xy_dif+[l-col], xy_sum+[l+col])
#         result = []
#         DFS([], [], [])
#         return [["."*j + 'Q' + "."*(n-j-1)for j in i] for i in result]
class Solution:
    def solveNQueens(self, n: int):
        def DFS(queens, xy_dif, xy_sum):
            l = len(queens)
            if l == n:
                result.append(queens)
                return
            for col in range(n):
                if col not in queens and l + col not in xy_sum and l - col not in xy_dif:
                    DFS(queens+[col], xy_dif+[l-col], xy_sum+[l+col])
        result = []
        DFS([], [], [])
        return [["."*j + 'Q' + "."*(n-j-1)for j in i] for i in result]


class Solution():
    def solveNQueens(self, n):
        if n < 1:return []
        self.result = []
        self.DFS(n,0,0,0,0,[])
        return self.result

    def DFS(self, n, row, cols, pie, na, cur_state):
        if row == n:
            self.result.append(cur_state)
            return
        # 得到当前所有的空位
        bits = (~(cols | pie | na) & (1 << n) - 1)
        while bits:
            #取到最低位的1 2 4 8
            p = bits & -bits
            #表示在位置p放皇后
            bits = bits & (bits - 1)#最后一个1变成0
            self.DFS(n, row+1, cols|p, (pie|p)<<1, (na|p)>>1, cur_state+[p])
s = Solution()
r = s.solveNQueens(4)
print(r)