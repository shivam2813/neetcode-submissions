class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        prefixSum=nums[0]
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefixSum*=nums[i]
            prefix[i]=prefixSum
        suffixSum=nums[n-1]
        suffix=[0]*n
        suffix[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffixSum*=nums[i]
            suffix[i]=suffixSum
        result = [1]*n
        result[0]=suffix[1]
        result[n-1]=prefix[n-2]
        for i in range(1,n-1):
            result[i]=prefix[i-1]*suffix[i+1]
        return result
