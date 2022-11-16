class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 计算 gas - cost的cumsum 一旦遇到<0 直接从下一个开始
        if sum(gas) < sum(cost):return -1
        cumsum = 0
        start = 0
        for i in range(len(gas)):
            cumsum += gas[i] - cost[i]
            if cumsum < 0:
                start = i + 1
                cumsum = 0
        return start
