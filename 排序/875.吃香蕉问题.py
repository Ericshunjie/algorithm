class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # 暴力搜索
        # for k in range(2, max_p):
        #     # 速度为k
        #     # 计算用的时间
        #     # print(k)
        #     tmp_result = 0
        #     for p in piles:
        #         tmp_result += p // k + 1 if p % k else p // k
        #     # print(tmp_result)
        #     if tmp_result == h:
        #         return k
        # 暴力法知道速度k 下 吃掉piles 的时间 是成正比的
        # 可以用二分法搜索k 下界为1 上界是max(piles)
        # 当 time > h : 说明h内吃不完 k = mid +1
        # 当 time <=h:说明吃完了还有空余时间 k可以变小 max_p = mid

        n = len(piles)
        l = 1
        max_p = max(piles)

        while l < max_p:
            k = (l + max_p) >> 1
            tmp_result = 0
            for p in piles:
                tmp_result += p // k + 1 if p % k else p // k
            if tmp_result <= h:
                max_p = k
            else:
                l = k + 1
        return l


