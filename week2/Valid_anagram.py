# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         result_dict = {}
#         for i in s:
#             if i in result_dict.keys():
#                 result_dict[i] += 1
#             else:
#                 result_dict[i] = 1
#         for j in t:
#             if j in result_dict.keys():
#                 result_dict[j] -= 1
#             else:
#                 result_dict[j] = -1

#         for k,v in result_dict.items():
#             if v != 0:
#                 return False
#         return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s = list(s)
#         s.sort()
#         t = list(t)
#         t.sort()
#         print(s,t)
#         return "".join(s) == "".join(t)
# s = Solution()
# s.isAnagram('a', 'b')


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


"""
方法一：
使用HashMap      python中dict数据类型
对第一个str count ++
对第二个str count --  最后看dict是否为空

方法二：
排序后比较

方法三：
python内置函数sorted使用    #sorted
sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

方法四：
方法一的改进 
0、先判断长度是否一致 
1、用一个长度为26的list代替dict 
2、在遍历t的时候 发现小于0的直接返回False
在python中执行结果
"""
