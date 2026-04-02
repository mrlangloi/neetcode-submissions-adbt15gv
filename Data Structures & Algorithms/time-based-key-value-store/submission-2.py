class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        currMap = self.timemap[key]
        res = ""
        l = 0
        r = len(currMap) - 1

        while l <= r:
            m = l + (r - l) // 2
            if currMap[m][0] <= timestamp:
                res = currMap[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
