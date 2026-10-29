class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t
        
        countT = defaultdict(int)
        window = defaultdict(int)

        for char in t:
            countT[char] += 1
        
        res = [-1, -1]
        resLen = math.inf

        l = 0
        r = 0
        have = 0
        need = len(countT)

        while r < len(s):
            window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r + 1]
                window[s[l]] -= 1
                if countT[s[l]] > 0 and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1

        return s[res[0]:res[1]]
                
            
