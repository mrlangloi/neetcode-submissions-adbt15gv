class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.timemap[key]) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            if self.timemap[key][m][1] <= timestamp:
                res = self.timemap[key][m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
