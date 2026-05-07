class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}
        for i in range(len(nums)):
            currentRem=target-nums[i];
            if currentRem in data:
                return [data[currentRem],i]
            data[nums[i]]=i
        return []
