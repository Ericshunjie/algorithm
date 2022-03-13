# class Solution:
#     def rotate(self, nums,k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             n = nums.pop()
#             nums.insert(0, n)
#         return nums

# class Solution:
#     def rotate(self, nums,k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         for _ in range(k):
#             tmp = nums[-1]
#             i = len(nums) - 1
#             while i != 0:
#                 nums[i] = nums[i - 1]
#                 i -= 1
#             nums[i] = tmp

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums = self.reverse(nums, 0, len(nums)-1)
        nums = self.reverse(nums, 0, k-1)
        nums = self.reverse(nums, k, len(nums)-1)
        return nums
        
    def reverse(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1
        return nums
        
s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))



"""
方法1：
利用python的list内置函数 直接将末尾的数字insert到第0个位置

方法2：
暴力法 自己实现单词旋转  其实是可以的   leetcode上超出时间限制

方法3：
数组反转 最后的结果总是把数组的最后 k%len(nums)个 元素放在最前面 剩余前面的往后挪动
可以先把整体反转再把前面 k%len(nums)个，再把后面反转即可
"""