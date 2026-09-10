class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        result = []
        intervals.sort(key =lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        ans = intervals[0]
        for i in range(1,len(intervals)):
            if end >= intervals[i][0]:
                end = max(end,intervals[i][1])
            else:
                result.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start,end])
        return result