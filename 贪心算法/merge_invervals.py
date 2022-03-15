class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])

        merges = []
        for interval in intervals:
            if not merges or interval[0] > merges[-1][1]:
                merges.append(interval)
            else:
                merges[-1][1] = max(interval[1], merges[-1][1])
        return merges