class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == t:
            return s
        freq1 = {}
        for i in range(len(t)):
            freq1[t[i]] = freq1.get(t[i],0)+1
        freq2 = {}
        result = ""
        left = 0
        required = len(freq1)
        mini = float('inf')
        formed = 0
        for right in range(len(s)):
            freq2[s[right]] = freq2.get(s[right],0)+1
            if s[right] in freq1 and freq1[s[right]] == freq2[s[right]]:
                formed += 1
            while formed == required:
                if right - left + 1 < mini:
                    mini = right-left+1
                    result = s[left:right+1]
                freq2[s[left]] -= 1
                if s[left] in freq1 and freq1[s[left]] > freq2[s[left]]:
                    formed -= 1
                left += 1
        return result