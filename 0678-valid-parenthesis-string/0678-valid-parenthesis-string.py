class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0
        for i in s:
            if i == '(':
                low += 1
                high += 1
            elif i == '*':
                low -= 1
                high += 1
                low = max(low,0)
            else:
                low -= 1
                high -= 1
                low = max(low,0)
            if high < 0:
                return False
        return low == 0
    