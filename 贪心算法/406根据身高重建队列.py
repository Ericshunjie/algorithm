class Solution:
    def reconstructQueue(self, people):
        # 两个维度需要考虑，先排序搞定其中一个，在解决另一个维度

        # 先按照身高降序排序 按照k升序排列 前面的人身高一定比后面的高
        people.sort(key=lambda x:(-x[0], x[1]))
        print(people)
        result = []
        n = len(people)
        for i in range(n):
            result.insert(people[i][1], people[i])
            print(result)
        return result

s = Solution()
s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])