class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 回溯 深度优先
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        def dfs(board, used, px,py,words):
            if board[px][py] != words[0]:
                return False
            # 注意这个时候 px py还没有使用，words==board[px][py]就可以结束了 如果定义的是还没用 就是0
            if len(words) == 1:
                return True
            used[px][py] = 1
            result = False
            for jj in range(4):
                pxx = px + dx[jj]
                pyy = py + dy[jj]
                if 0<=pxx<rows and 0<=pyy<cols and used[pxx][pyy] == 0:
                    state = dfs(board, used,pxx,pyy,words[1:])
                    if state:
                        result = True
                        break
            used[px][py] = 0
            return result
        rows = len(board)
        cols = len(board[0])
        used = [[0] * cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if dfs(board, used, i,j,word):
                    return True
        return False