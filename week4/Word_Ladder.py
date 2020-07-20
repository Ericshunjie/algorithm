class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        l = len(beginWord)
        used = {}
        for i in wordList:
            used[i] = 0
        all_class = {}
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                if word[:i] + '*' + word[i+1:] in all_class:
                    all_class[word[:i] + '*' + word[i+1:]].append(word)
                else:
                    all_class[word[:i] + '*' + word[i+1:]] = [word]

        queue = [(beginWord, 1)]
        while queue:
            cur, level = queue.pop(0)
            if cur == endWord:
                return level
            for i in range(L):
                tmp = cur[:i] + '*' + cur[i+1:]
                if tmp not in all_class:
                    continue
                for word in all_class[tmp]:
                    if word == endWord:
                        return level + 1
                    if not used[word]:
                        queue.append((word, level+1))
                        used[word] = 1
        return 0
# 构建一个hashmap 建立bank里面汉明距离为1的索引关系
# used用来记录是否被用过 避免无限循环
# 广度优先遍历 队列实现
