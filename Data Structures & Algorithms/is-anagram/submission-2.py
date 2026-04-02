class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        for sChar in s:
            if sChar not in s_freq:
                s_freq[sChar] = 1
            else:
                s_freq[sChar] += 1
        
        t_freq = {}
        for tChar in t:
            if tChar not in t_freq:
                t_freq[tChar] = 1
            else:
                t_freq[tChar] += 1
        
        return s_freq == t_freq