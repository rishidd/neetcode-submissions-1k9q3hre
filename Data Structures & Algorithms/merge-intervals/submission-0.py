class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        print(intervals)
        
        for bounds in intervals:
            print(bounds[1])
            if not res or res[-1][1] < bounds[0]:
                res.append(bounds)
            else:
                res[-1][1] = max(res[-1][1], bounds[1])
        print(res)
    
        return res
