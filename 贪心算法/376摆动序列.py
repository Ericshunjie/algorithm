# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
#
# 例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
#
# 给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

class Solution:
    def wiggleMaxLength(self, nums) -> int:
        # 贪心：遍历每个点看是不是峰值，不是峰值删除
        # 注意两端的情况
        n = len(nums)
        if n <= 1:return n
        preDiff = 0
        result = 1 # 默认最后一个是一个峰值
        for i in range(n-1):
            curDiff = nums[i+1] - nums[i]
            if (curDiff > 0 and preDiff<=0) or (curDiff <0 and preDiff >= 0):
                # 峰值 注意curDiff=0的情况，此时不是峰值
                result += 1
                preDiff = curDiff
            else:
                # 不是峰值 删除 preDiff不变
                pass
        return result

s = Solution()
r = s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])