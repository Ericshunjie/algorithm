class Solution:
    def candy(self, ratings) -> int:
        ## 贪心 从局部最优到全局最优
        # 首先从左到右 考虑右边大于左边的情况 candyvec[i+1] = candyvec[i] + 1
        # 然后从右到左 考虑左边大于右边的情况  caandyvec[i] = max(caandyvec[i], candyvec[i+1]+1)
        # 为什么第二次考虑的时候要从右到左 ，因为假如第一个大于第二个 那么第一个更新之后 看第二的时候 第二个需要更新的话还要回头更新第一个
        # 总结来说就是不能利用之前的结果
        n = len(ratings)
        candyvec = [1] * n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candyvec[i] = candyvec[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candyvec[i] = max(candyvec[i], candyvec[i+1] + 1)
        return sum(candyvec)