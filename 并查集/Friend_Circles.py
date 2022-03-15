class Solution:
    def findCircleNum(self, M) -> int:
        if len(M) == 0:
            return 0
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)
        return len(set([self._find(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._find(p, i)
        p2 = self._find(p, j)
        if p1 != p2:
            p[p1] = p2

    def _find(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            tmp = p[i]
            p[i] = root
            i = tmp
        return root
s = Solution()
r = s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(r)