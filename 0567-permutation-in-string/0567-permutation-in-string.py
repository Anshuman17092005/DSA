class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left = 0
        freq1 = {}
        for i in range(len(s1)):
            freq1[s1[i]] = freq1.get(s1[i],0)+1
        freq2 = {}
        left = 0
        for right in range(len(s2)):
            freq2[s2[right]] = freq2.get(s2[right],0) + 1
            while (right-left+1) > len(s1):
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if freq1 == freq2:
                return True
        return False