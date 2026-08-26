class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            curr = [0] * (i+1)
            for j in range(i+1):
                if j == 0:
                    curr[j] = 1
                elif j == i:
                    curr[j] = 1
                else:
                    curr[j] = prev[j-1] + prev[j]
            prev = curr
            result.append(curr)
        return result