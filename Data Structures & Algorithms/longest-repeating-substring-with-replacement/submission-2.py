class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        highest_freq = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            highest_freq = max(highest_freq, freq[s[r]])
            while r - l + 1 - highest_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res