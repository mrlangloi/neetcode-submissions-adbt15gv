class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + '#' + string

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        end = i + 1

        # 5#Hello5#World
        while i < len(s):
            while s[end].isdigit():
                end += 1
            length = int(s[i:end])
            res.append(s[end + 1:end + length + 1])
            i = end + length + 1
            end = i + 1
        
        return res

