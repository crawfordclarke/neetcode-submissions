class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        myHeap = []


        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(myHeap, (distance, [x, y]))

        
        res = []

        for _ in range(k):
            distance, point = heapq.heappop(myHeap)
            res.append(point)

        return res



        
        