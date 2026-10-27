class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for s in range(len(s1)):
            s1Count[ord(s1[s]) - ord('a')] += 1
            s2Count[ord(s2[s]) - ord('a')] += 1
        
        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:
            if s1Count == s2Count:
                return True
            
            r += 1
            s2Count[ord(s2[r]) - ord('a')] += 1
            s2Count[ord(s2[l]) - ord('a')] -= 1
            l += 1


        return s1Count == s2Count