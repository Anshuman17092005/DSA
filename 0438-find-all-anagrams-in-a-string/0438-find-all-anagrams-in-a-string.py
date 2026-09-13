class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        freq1 = {}
        for i in range(len(p)):
            freq1[p[i]] = freq1.get(p[i],0) + 1
        freq2 = {}
        left = 0
        for right in range(len(s)):
            freq2[s[right]] = freq2.get(s[right],0) + 1
            while right-left+1 > len(p):
                freq2[s[left]] -= 1
                if freq2[s[left]] == 0:
                    del freq2[s[left]]
                left += 1
            if freq1 == freq2:
                result.append(left)
        return result