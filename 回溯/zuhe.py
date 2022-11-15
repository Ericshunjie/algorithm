class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 回溯 dfs
        def dfs(level, k, cur):
            if level == k:
                result.append(cur)
                return

            for i in range(1, n + 1):
                if len(cur) == 0 or (i not in cur and i > cur[-1]):
                    dfs(level + 1, k, cur + [i])
        result = []
        dfs(0, k, [])
        return result