class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(s1_len):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        l = 0
        r = s1_len
        
        for r in range(r, s2_len):
            if s1_count == s2_count:
                return True
            
            s2_count[ord(s2[r]) - ord('a')] += 1
            s2_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            
        return s1_count == s2_count