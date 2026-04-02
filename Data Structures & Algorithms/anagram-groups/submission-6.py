class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = dict()
        ord_a = ord('a')

        for string in strs:
            char_arr = [0 for _ in range(26)]
            for c in string:
                char_arr[ord(c) - ord_a] += 1
            key = tuple(char_arr)
            char_map.setdefault(key, []).append(string)
        
        res = []

        for values in char_map.values():
            res.append(values)
        
        return res