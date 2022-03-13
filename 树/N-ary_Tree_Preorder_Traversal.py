"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
        
#         result = [root.val,]
#         for c in root.children:
#             result.extend(self.preorder(c))
#         return result

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root, ]
        result = []

        while stack:
            root = stack.pop()
            result.insert(0, root.val)
            stack.extend(root.children)
        return result



"""
方法一：递归

方法二：迭代  主要理解二叉树后续遍历方案  广度优先思想

"""