class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for j in range(1,len(strs)):
            i = 0
            while i < len(prefix) and i < len(strs[j]) and prefix[i] == strs[j][i]:
                i += 1
            prefix = prefix[:i]
            if prefix == "":
                return ""
        return prefix