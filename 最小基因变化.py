class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def dif_num(s1, s2):
            c = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    c += 1
            return c

        queue = [start, ]
        used = {start: 0}
        for i in bank:
            used[i] = 0
        result = 0
        while queue:

            for _ in range(len(queue)):
                start = queue.pop(0)
                used[start] = 1
                if start == end:
                    return result
                for i in range(len(bank)):
                    if dif_num(start, bank[i]) == 1 and not used[bank[i]]:
                        queue.append(bank[i])

            result += 1
        return -1