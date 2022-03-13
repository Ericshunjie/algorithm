class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        for i in range(n):
            station = i
            all_gas = 0
            while all_gas >= 0:
                all_gas += gas[station]

                next_cost = cost[station]

                all_gas -= next_cost
                if all_gas < 0:
                    break

                station += 1
                station %= n
                if station == i:
                    break
            if all_gas >= 0:
                return i
        return -1

s = Solution()
r = s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])