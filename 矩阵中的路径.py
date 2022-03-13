class Solution:
    def exist(self, board, word: str) -> bool:
        dx = [-1,0,0,1]
        dy = [0,1,-1,0]
        def dfs(board,used,px,py,word):
            if len(word) == 0:
                return True
            ch = word[0]
            if board[px][py] == ch:
                tmp = []
                for jj in range(4):

                    pnx, pny = px + dx[jj], py + dy[jj]
                    if 0 <= pnx < rows and 0 <= pny < cols and not used[pnx][pny]:
                        used[pnx][pny] = 1
                        tmp.append(dfs(board,used,pnx,pny,word[1:]))
                        used[pnx][pny] = 0
                if True in tmp:
                    return True
                else:
                    return False

            else:
                return False
        rows = len(board)
        cols = len(board[0])
        used = [[0] * cols for _ in range(rows)]
        used[0][0] = 1
        return dfs(board, used,0,0, word)
s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")

