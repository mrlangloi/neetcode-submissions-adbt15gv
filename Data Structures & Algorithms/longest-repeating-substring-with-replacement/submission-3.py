class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = [0] * 26
        maxF = 0
        l = 0
        
        for r in range(len(s)):
            chars[ord(s[r]) - ord('A')] += 1
            maxF = max(maxF, chars[ord(s[r]) - ord('A')])
            while (r - l + 1) - maxF > k:
                chars[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res

