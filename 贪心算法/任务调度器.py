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

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 排序后的贪心
        # 取计数最多的字母，(maxcount -1) *(n+1) + 1是正常状态下的结果
        # 但是，一、会有计数等于最多字母的情况 比如A3个B3个 ，此时 (maxcount -1) *(n+1) + max_count
        # 另一种情况是 如果(maxcount -1) *(n+1) + max_count 之后还有没有填充的任务，
        # 这时候取 count_all 随便放都可以
        counts = {}
        for ch in tasks:
            counts[ch] = counts.get(ch,0) + 1
        max_nums = max(counts.values())
        max_count = 0
        for i in counts.values():
            if i == max_nums:
                max_count += 1
        return max(len(tasks), (max_nums - 1) * (n+1) + max_count)

s = Solution()
r = s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)