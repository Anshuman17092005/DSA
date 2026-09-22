class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        maxi = 0
        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            maxi = max(maxi,right-left+1)
            seen.add(s[right])
        return maxi 