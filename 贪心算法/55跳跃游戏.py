class Solution:
    def canJump(self, nums):
        n = len(nums)
        if n <= 1:return True
        rightmost = 0
        i = 0
        while i <= rightmost:
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return True
            i += 1
        return False
s = Solution()
r = s.canJump([2,3,1,1,4])
print(r)