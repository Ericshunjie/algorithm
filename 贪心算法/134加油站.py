class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        ## 贪心 求cumsum 一旦小于0则区间内所有的点不可能为起点，起点从i+1开始计算

        start = 0
        total_sum = 0
        cumsum = 0
        n = len(gas)
        for i in range(n):
            total_sum += gas[i] - cost[i]
            cumsum += gas[i] - cost[i]

            if cumsum < 0:
                cumsum = 0
                start = i + 1
        if total_sum < 0:return -1
        return start
