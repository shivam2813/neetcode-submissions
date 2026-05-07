class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        for i in range(len(nums)):
            res=1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    res*=nums[j]
            result[i]=res
        return result