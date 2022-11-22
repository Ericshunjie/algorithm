class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        def cal_diff(s1, s2):
            n = len(s1)
            c = 0
            for i in range(n):
                if s1[i] != s2[i]:
                    c += 1
            return c
        if startGene == endGene:return 0
        queue = [startGene,]
        bank_len = len(bank)
        used = [0] * bank_len
        res = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for i in range(bank_len):
                    if not used[i] and cal_diff(cur, bank[i])==1:
                        queue.append(bank[i])
                        used[i] = 1
                        if bank[i] == endGene:
                            return res + 1
            res += 1
        return -1
