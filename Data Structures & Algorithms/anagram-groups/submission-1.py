class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = dict()

        for word in strs:
            alphaList = [0] * 26
            for c in word:
                alphaList[ord(c) - ord('a') - 1] += 1
            key = tuple(alphaList)
            if key not in char_map:
                char_map[key] = [word]
            else:
                char_map[key].append(word)
        
        res = []

        for value in char_map.values():
            res.append(value)

        return res