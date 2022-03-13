class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        n = len(s)
        index_s = 0
        res = 0
        for i in range(n):
            if index_s < len(g) and g[index_s] <= s[i]:
                # manzu
                res += 1
                index_s += 1
        return index_s