class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(1,len(nums)):
            if not nums[i] == nums[j]:
                nums[j+1] = nums[i]
                j += 1
        return j+1

s = Solution()
print(s.removeDuplicates([1,1,3,5,6,6,7]))



# 1 快慢指针 遍历数组 和前面的数比较 相同就删除
# j指向不重复的位置  遍历 i 与j指向数字大小一样就pass 不一样就把j+1换成i的值 j+=1