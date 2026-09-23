class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        freq1 = {}
        freq2 = {}
        for i in s1:
            freq1[i] = freq1.get(i,0)+1
        left = 0
        for right in range(len(s2)):
            freq2[s2[right]] = freq2.get(s2[right],0)+1
            while right-left+1 > len(s1):
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if freq1 == freq2:
                return True
        return False