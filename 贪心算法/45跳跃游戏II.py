class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        if n <= 1:return 0
        rightmost = 0
        end = 0 #标兵 代表当前步数下能到的最远的右边，只有在i=end的时候end变成此时的rightmost
        result = 0
        for i in range(n-1):
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return result + 1
            if i == end:
                result += 1
                end = rightmost
        return result