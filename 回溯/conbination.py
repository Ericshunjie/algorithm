class Solution:
    def combine(self, n: int, k: int):
        self.result = []
        self.generator(0, k, [], n)
        return self.result

    def generator(self, level, k, ans, n):
        if level == k:
            self.result.append(ans)
            return
        for i in range(1,n+1):
            if len(ans)==0 or (i not in ans and i > ans[-1]):
                self.generator(level+1, k, ans+[i], n)