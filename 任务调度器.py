class Solution:
    def leastInterval(self, tasks, n) -> int:
        if n == 0:
            return len(tasks)
        counter = {}
        for t in tasks:
            counter[t] = counter.get(t, 0) + 1
        counter_sort = sorted(counter.items(), key=lambda x : -x[1])
        i = 0
        result = []
        seg =  n + 1
        while i < len(tasks):
            if seg < n + 1:
                result.append(0)
                seg += 1
            else:
                seg = 0
                for k in counter_sort:
                    v = counter[k[0]]
                    if v > 0 :
                        result.append(k[0])
                        i += 1
                        seg += 1
                        counter[k[0]] -= 1
        print(result)
        return len(result)
s = Solution()
r = s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)