class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = dict()

        for string in strs:
            char_arr = [0 for _ in range(26)]
            for c in string:
                char_arr[ord(c) - ord('a')] += 1
            key = tuple(char_arr)
            char_map.setdefault(key, [])
            char_map.get(key).append(string)
        
        res = []

        for values in char_map.values():
            res.append(values)
        
        return res