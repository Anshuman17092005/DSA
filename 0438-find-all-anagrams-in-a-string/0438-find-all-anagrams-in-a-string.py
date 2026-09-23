class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq1 = {}
        for i in p:
            freq1[i] = freq1.get(i,0)+1
        freq2 = {}
        result = []
        left = 0
        for right in range(len(s)):
            freq2[s[right]] = freq2.get(s[right],0)+1
            while right-left+1 > len(p):
                freq2[s[left]] -= 1
                if freq2[s[left]] == 0:
                    del freq2[s[left]]
                left += 1
            if freq1 == freq2:
                result.append(left)
        return result