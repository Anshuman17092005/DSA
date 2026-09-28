class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            '{':'}',
            '[':']',
            '(':')'
        }
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack or pairs[stack[-1]] != i:
                    return False
                stack.pop()
        if stack:
            return False
        return True