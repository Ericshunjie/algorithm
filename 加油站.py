class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # cumsum 小于0直接从下一个开始

        cumsum = 0
        totalsum = 0
        n = len(gas)
        start = 0
        for i in range(n):
            cumsum += gas[i] - cost[i]
            totalsum += gas[i] - cost[i]
            if cumsum < 0:
                start = i + 1
                cumsum = 0
        if sum(gas) < sum(cost):return -1
        return start

s = Solution()
r = s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])