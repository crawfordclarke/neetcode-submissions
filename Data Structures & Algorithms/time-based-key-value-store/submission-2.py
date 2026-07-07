class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []

        self.time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        timelist = self.time_map[key]

        l,r = 0, len(timelist) -1
        minseen = ""
        while l <= r:
            mid = (l + r)//2

            if timelist[mid][1] > timestamp:
                r = mid - 1
            if timelist[mid][1] <= timestamp:
                minseen = timelist[mid][0]
                l = mid + 1
        return minseen






        

        



        
        
