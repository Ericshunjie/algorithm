class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """

        ## 回溯+剪枝
        # traceback函数代表当前index 能否组成斐波那契数

        def backtrace(index):
            if index == len(num):
                # 如果index到达最后一个，此时len(result)>=3就可以返回result
                return len(result) >= 3
            # 开始回溯
            cur = 0
            for i in range(index, len(num)):
                # 如果这个数以0开头 那么就是一个无效的数字
                if i > index and num[index] == '0':
                    break

                cur = cur * 10 + int(num[i])
                if cur > 2 ** 31 - 1:
                    break
                if len(result) >= 2 and cur > result[-1] + result[-2]:
                    break
                if len(result) < 2 or cur == result[-1] + result[-2]:
                    result.append(cur)
                    if backtrace(i + 1):
                        return True
                    result.pop()
            return False

        result = []
        backtrace(0)
        return result
