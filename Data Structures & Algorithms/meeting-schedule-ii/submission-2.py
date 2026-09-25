"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        end =[interval.end for interval in intervals]

        start.sort()
        end.sort()

        s, e = 0,0

        count = 0
        max_count = 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                max_count = max(count, max_count)
                s += 1
            else:
                count -= 1
                e += 1
        return max_count        

    


