class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        heap = []
        time = 0
        q = deque()

        for task in tasks:
            freq[task] += 1

        for count in freq.values():
            heapq.heappush(heap, -count)    
        

        while heap or q:
            time += 1

            while q and q[0][1] == time:
                heapq.heappush(heap, (q[0][0]))
                q.popleft()

            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    q.append((count, time + n + 1))
        return time            












        
        