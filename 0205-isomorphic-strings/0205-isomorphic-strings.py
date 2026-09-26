class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] in map1 and t[i] != map1[s[i]]:
                return False
            if t[i] in map2 and s[i] != map2[t[i]]:
                return False
            map1[s[i]] = t[i]
            map2[t[i]] = s[i]
        return True