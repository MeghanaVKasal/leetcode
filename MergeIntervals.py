from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return
        intervals.sort()
        ps, pe = intervals[0]
        res = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= pe:
                ps = min(s,ps)
                pe = max(e,pe)
                res[-1] = [ps,pe]
            else:
                res.append([s,e])
                ps,pe = s,e
        return res

input = [[[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]], [[1,4],[0,0]],[[1,4],[4,5]]]
expected =  [[[1,6],[8,10],[15,18]], [[1,5]], [[0,0],[1,4]],[[1,5]]]
for i,inp in enumerate(input):
    print("output:   ", Solution().merge(inp))
    print("expected: ", expected[i])
    print("---------------------------")
