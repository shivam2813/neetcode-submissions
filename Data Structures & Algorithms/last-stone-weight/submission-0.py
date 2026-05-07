import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-(stone))
        
        while len(heap)>0:
            if len(heap)==1:
                return -heap[0]
            maxV=heapq.heappop(heap)
            secondmaxV=heapq.heappop(heap)
            diff=(-(maxV))-(-(secondmaxV))
            if diff>0:
                heapq.heappush(heap,-(diff))
        
        return 0