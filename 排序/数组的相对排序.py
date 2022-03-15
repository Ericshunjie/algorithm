class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = [0] * 1000
        for i in range(len(arr1)):
            count[arr1[i]] += 1
        print(count[:15])
        k = 0
        for i in range(len(arr2)):
            while count[arr2[i]] > 0:
                arr1[k] = arr2[i]
                k += 1
                count[arr2[i]] -= 1
        print(arr1)
        for i in range(len(count)):
            while count[i] > 0:
                arr1[k] = i
                k += 1
                count[i] -= 1
        return arr1
s = Solution()
r = s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])
print(r)