class Solution:
    def groupAnagrams(self, strs):

        result = {}
        for s in strs:
            key = tuple(sorted(s))
            result[key] = result.get(key, []) + [s]
        return list(result.values())

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


"""



"""