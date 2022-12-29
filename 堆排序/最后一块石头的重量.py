import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 大顶堆
        q = [-stone for stone in stones]
        heapq.heapify(q)

        while len(q) > 1:
            x = heapq.heappop(q)
            y = heapq.heappop(q)
            if x != y:
                heapq.heappush(q, x-y)
        return -q[0] if len(q) == 1 else 0