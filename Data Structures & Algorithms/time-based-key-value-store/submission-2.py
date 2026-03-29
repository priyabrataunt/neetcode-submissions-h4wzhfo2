class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        
        left = 0
        right = len(values) - 1
        
        while left <= right:
            mid = (left + right) // 2
            stored_timestamp = values[mid][1]
            
            if stored_timestamp <= timestamp:
                result = values[mid][0]  # potential answer found!
                left = mid + 1           # but search right for better answer
            else:
                right = mid - 1          # too big, search left
        
        return result