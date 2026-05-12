class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data={}
        
        for i in nums:
            if i not in data:
                data[i]=0
            data[i]+=1
        
        sortedDict=dict(sorted(data.items(),key=lambda item:item[1],reverse=True))
        result=[]
        for key, value in sortedDict.items():
            # print(key)
            # print(value)
            if len(result)<k:
                result.append(key)
            else:
                break

        return result