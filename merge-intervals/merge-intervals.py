class Solution:
    def isOverlaping(a,b,c,d):
        # (a,...  c ...,b)   d?
        return a <= c <= b
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        l,r = intervals.pop(0)
        merged = []
        unclosed_start = l
        latest_end = r
        while intervals:
            l,r = intervals.pop(0)
            if Solution.isOverlaping(unclosed_start, latest_end, l, r):
                latest_end = max(latest_end,r)
            else:
                merged.append([unclosed_start, latest_end])
                unclosed_start = l
                latest_end = r
        merged.append([unclosed_start, latest_end])
        return merged
        