class Solution:
    def maxArea(self, height) -> int:
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