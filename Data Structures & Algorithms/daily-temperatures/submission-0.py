class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0] * n
        stackd=[]

        for i in range(n):
            while stackd and temperatures[i]> temperatures[stackd[-1]]:
                idx=stackd.pop()
                result[idx]=i-idx
            stackd.append(i)
        
        return result
            