class Solution:
    def maxArea(self, height) -> int:
        # 双指针
        # 贪心：短边向中间靠 因为面积取最矮高度*底
        result = 0
        i,j = 0, len(height)-1
        while i < j:
            area = min(height[i], height[j]) * (j-i)
            result = max(area, result)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))