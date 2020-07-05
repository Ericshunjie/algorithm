"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#     def levelOrder(self, root):
#         if not root:
#             return root
#         flag = 0
#         queue = [(root, flag), ]
#         result = []
#         old_flag = -1
#         while queue:
#             root, flag = queue.pop(0)
#             queue.extend([(i,flag+1) for i in root.children])
#             if flag != old_flag:
#                 result.append([root.val])
#             else:
#                 result[-1].append(root.val)
#             old_flag = flag    
#         return result


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root, ]
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                level.append(root.val)
                queue.extend(root.children)
            result.append(level)
        return result


        

"""
方法一：队列解决 通过flag,old_flag两个标量分别表示当前节点层级，上一节点层级，用来判断当前节点属于新的一层还是旧的一层


方法二：还是队列解决，没到下一层，len(queue)可以记录节点个数
"""