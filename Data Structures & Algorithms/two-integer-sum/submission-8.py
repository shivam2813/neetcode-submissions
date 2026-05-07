class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}
        for i,n in enumerate(nums):
            currentRem=target-n;
            if currentRem in data:
                return [data[currentRem],i]
            data[n]=i
        return []
