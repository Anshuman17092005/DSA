class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = {
            '{':'}',
            '[':']',
            '(':')'
        }
        result = []
        for ch in s:
            if ch in stack:
                result.append(ch)
            else:
                if not result or stack[result[-1]] != ch:
                    return False
                result.pop()
        return len(result) == 0