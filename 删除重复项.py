class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针
        # slow 指向即将写入新数字的位置，也代表新数组的长度 fast代表正在检查的这数字
        # 什么样的情况下需要写入新数字：
        # 什么情况不写数字，直接跳过：
        # 考虑到 数组递增,而且允许出现两次  当且仅当nums[fast]==nums[slow-2]时，这时候fast要跳过
        n = len(nums)
        if n <= 2: return n
        slow = 2
        fast = 2
        while fast < n:
            # 检查fast这个数字应不应该被保留
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
