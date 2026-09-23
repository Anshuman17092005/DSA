class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq1 = {}
        for i in t:
            freq1[i] = freq1.get(i,0)+1
        left = 0
        freq2 = {}
        result = ""
        mini = float('inf')
        required = len(freq1)
        formed = 0
        for right in range(len(s)):
            freq2[s[right]] = freq2.get(s[right],0)+1
            if s[right] in freq1 and freq1[s[right]] == freq2[s[right]]:
                formed += 1
            while formed == required:
                if right-left+1<mini:
                    mini = right-left + 1
                    result = s[left:right+1]
                freq2[s[left]] -= 1
                if s[left] in freq1 and freq2[s[left]] < freq1[s[left]]:
                    formed -= 1
                left += 1
        return result