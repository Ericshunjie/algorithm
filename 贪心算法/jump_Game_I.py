class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        rightmost = 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i+nums[i])
                if rightmost >= n-1:
                    return True
            else:
                return False
        # return False

# 遍历每一个点
# 记录当点能走的最远位置 rightmost
# 当 i > rightmost的时候 已经不可能到最后位置了

# 当rightmost 大于len 的时候 可以到达