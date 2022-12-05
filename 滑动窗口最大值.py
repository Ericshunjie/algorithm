class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #遍历的方法复杂度为 nk 超时
        # 利用大顶堆数据结构 可以优化成nlog(k)

        # 先将k个数据放入大顶堆
        n = len(nums)
        q = [(-nums[i], i)for i in range(k)]
        heapq.heapify(q)
        res = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            # 当堆顶的index 小于等于 i-k的时候，这个元素需要pop
            while q[0][1] <= i-k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res