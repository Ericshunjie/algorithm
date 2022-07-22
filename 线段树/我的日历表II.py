from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        #用一个排序的dict value是该点加入日历的次数，start+1 end-1
        # 遍历所有的key,value
        # 用maxBook记录每个点被添加的次数，遇到起点添加，遇到终点减小
        # 当maxBook>2的时候，说明这个点超过2次发生三重预定了，则返回False，并且要把这个区间移除sortDict
        self.cnt = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.cnt[start] = self.cnt.get(start, 0) + 1
        self.cnt[end] = self.cnt.get(end, 0) - 1

        maxBook = 0
        for c in self.cnt.values():

            maxBook += c
            if maxBook > 2:
                self.cnt[start] = self.cnt.get(start, 0) - 1
                self.cnt[end] = self.cnt.get(end, 0) + 1
                return False
        return True


class MyCalendarTwo:

    def __init__(self):
        self.books = []
        self.overlaps = []


    def book(self, start: int, end: int) -> bool:

        for s,e in self.overlaps:
            # 如果start,end存在与overlap有交集的区间,则发生三重预定
            if start < e and end > s:
                return False

        # 不存在则可以添加
        for s,e in self.books:
            if start < e and end > s:
                self.overlaps.append([max(s,start),min(e,end)])
        self.books.append([start,end])

        return True





# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)