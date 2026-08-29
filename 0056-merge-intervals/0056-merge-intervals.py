class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x:x[0])
        result = []
        current = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= current[1]:
                current = [current[0],max(intervals[i][1],current[1])]
            else:
                result.append(current)
                current = intervals[i]
        result.append(current)
        return result